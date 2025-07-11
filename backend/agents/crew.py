"""
File: crew.py
Author: Wagner Pinheiro
Date: 2025-07-11
Last Modified: 2025-07-11

Purpose:
    This script orchestrates the entire resume analysis process. It assembles
    the specialized agents, defines the analysis tasks, and runs the CrewAI crew.
    It is also responsible for parsing the outputs from each agent and aggregating
    them into a final, structured response.

Dependencies:
    - json
    - crewai
    - All agent definitions (e.g., ats_agent)
    - agents.tasks
    - agents.schemas
"""
import json
from typing import List, Dict, Any
from crewai import Crew, Process
from .ats_agent import ats_agent, ATS_AGENT_WEIGHT
from .content_quality_agent import content_quality_agent, CONTENT_QUALITY_AGENT_WEIGHT
from .digital_presence_agent import digital_presence_agent, DIGITAL_PRESENCE_AGENT_WEIGHT
from .education_agent import education_agent, EDUCATION_AGENT_WEIGHT
from .projects_agent import projects_agent, PROJECTS_AGENT_WEIGHT
from .skills_agent import skills_agent, SKILLS_AGENT_WEIGHT
from .tailoring_agent import tailoring_agent, TAILORING_AGENT_WEIGHT
from .tasks import ResumeAnalysisTasks
from .schemas import AgentResponse, OverallAnalysisResponse

def parse_agent_output(task_output: Any) -> AgentResponse:
    """
    Parses the JSON string output from an agent task into an AgentResponse object.

    This function is robustly designed to handle various output formats from CrewAI,
    including raw JSON strings and JSON wrapped in markdown code blocks.

    Args:
        task_output (Any): The raw output from a CrewAI task execution.

    Returns:
        AgentResponse: A Pydantic model instance of the parsed agent response.
                       Returns a default error response if parsing fails.
    """
    # Task output can be a string or an object with a 'raw' attribute
    raw_output = getattr(task_output, 'raw', task_output)
    
    if not isinstance(raw_output, str):
        raw_output = str(raw_output)

    try:
        # The output from CrewAI tasks can sometimes be wrapped in markdown
        if raw_output.strip().startswith("```json"):
            json_str = raw_output.strip().split("```json")[1].split("```")[0].strip()
        else:
            json_str = raw_output
        
        response_dict = json.loads(json_str)
        return AgentResponse(**response_dict)
    except (json.JSONDecodeError, IndexError, TypeError) as e:
        print(f"Error parsing agent output: {e}\\nOutput was: {raw_output}")
        # Return a default error response
        return AgentResponse(
            score=0.0,
            feedback=["Failed to parse agent output."],
            suggestions=["Please check the agent's output format."],
            confidence=0.0
        )

def create_resume_analysis_crew(resume_content: str, job_description: str) -> Crew:
    """
    Creates and configures the CrewAI crew for resume analysis.

    This function dynamically assembles the team of agents and their
    corresponding tasks based on the resume and job description provided.

    Args:
        resume_content (str): The text content of the resume.
        job_description (str): The job description for tailoring analysis.

    Returns:
        Crew: A configured CrewAI Crew object, ready for execution.
    """
    tasks = ResumeAnalysisTasks()
    
    # Define all agents
    agents = {
        "ats": ats_agent,
        "projects": projects_agent,
        "skills": skills_agent,
        "tailoring": tailoring_agent,
        "digital_presence": digital_presence_agent,
        "content_quality": content_quality_agent,
        "education": education_agent,
    }

    # Define all tasks
    agent_tasks = [
        tasks.ats_formatting_task(agents["ats"], resume_content),
        tasks.projects_experience_task(agents["projects"], resume_content),
        tasks.skills_assessment_task(agents["skills"], resume_content),
        tasks.tailoring_task(agents["tailoring"], resume_content, job_description),
        tasks.digital_presence_task(agents["digital_presence"], resume_content),
        tasks.content_quality_task(agents["content_quality"], resume_content),
        tasks.education_task(agents["education"], resume_content),
    ]

    return Crew(
        agents=list(agents.values()),
        tasks=agent_tasks,
        process=Process.parallel,
        verbose=True,
    )

def run_resume_analysis(resume_content: str, job_description: str) -> OverallAnalysisResponse:
    """
    Runs the resume analysis crew and aggregates the results into a final response.

    This is the main entry point for the analysis process. It kicks off the crew,
    collects the results, calculates the weighted final score, and structures
    the data into a comprehensive response object.

    Args:
        resume_content (str): The text content of the resume.
        job_description (str): The job description for tailoring analysis.

    Returns:
        OverallAnalysisResponse: The final, aggregated analysis result.
    
    Raises:
        ValueError: If the number of task outputs does not match the number of agents.
    """
    resume_crew = create_resume_analysis_crew(resume_content, job_description)
    task_outputs: List[Any] = resume_crew.kickoff()

    # Define weights for aggregation
    weights = {
        "ats": ATS_AGENT_WEIGHT,
        "projects": PROJECTS_AGENT_WEIGHT,
        "skills": SKILLS_AGENT_WEIGHT,
        "tailoring": TAILORING_AGENT_WEIGHT,
        "digital_presence": DIGITAL_PRESENCE_AGENT_WEIGHT,
        "content_quality": CONTENT_QUALITY_AGENT_WEIGHT,
        "education": EDUCATION_AGENT_WEIGHT,
    }
    
    agent_names = list(weights.keys())
    
    # Ensure task_outputs align with agent_names if the order is guaranteed
    if len(task_outputs) != len(agent_names):
        raise ValueError("Mismatch between number of task outputs and agents.")

    analysis_details: Dict[str, AgentResponse] = {}
    category_scores: Dict[str, float] = {}
    final_score = 0.0
    
    # Assuming the order of task_outputs corresponds to the order of agent_tasks
    for i, agent_name in enumerate(agent_names):
        raw_output = task_outputs[i]
        parsed_response = parse_agent_output(raw_output)
        
        analysis_details[agent_name] = parsed_response
        category_scores[agent_name] = parsed_response.score
        
        # Calculate weighted score
        final_score += parsed_response.score * weights[agent_name] * 10 # Scale to 100

    # TODO: Implement a summary generation step using an LLM for a more cohesive overview.
    summary = f"Overall resume score is {final_score:.2f}/100. This is a placeholder summary."

    return OverallAnalysisResponse(
        final_score=final_score,
        category_scores=category_scores,
        analysis_details=analysis_details,
        summary=summary, # This could be generated by another LLM call for a better summary
    )
