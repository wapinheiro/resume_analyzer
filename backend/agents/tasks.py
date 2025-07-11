"""
File: tasks.py
Author: Wagner Pinheiro
Date: 2025-07-11
Last Modified: 2025-07-11

Purpose:
    This file defines the tasks for each agent in the resume analysis crew.
    Each task is responsible for invoking an agent to perform its specific
    analysis and ensuring the output is in a standardized JSON format.

Dependencies:
    - crewai
    - textwrap
    - agents.schemas
"""
from crewai import Task
from textwrap import dedent
from typing import Any
from crewai import Agent

class ResumeAnalysisTasks:
    """
    Defines the tasks for each agent in the resume analysis crew.
    Each task is responsible for invoking an agent to perform its specific analysis
    and returning the results in a standardized format.
    """

    def __format_expected_output(self) -> str:
        """
        Helper method to create a consistent and detailed JSON output format description.
        
        This structured prompt ensures that the LLM returns data in a predictable
        and parsable format.

        Returns:
            str: A string describing the required JSON output format.
        """
        return dedent("""\
        Your final answer MUST be a JSON object matching the following schema:
        {
            "score": "float (a score from 0.0 to 10.0)",
            "feedback": "list[str] (specific, constructive feedback points)",
            "suggestions": "list[str] (actionable recommendations for improvement)",
            "confidence": "float (your confidence in the analysis, from 0.0 to 1.0)"
        }
        """)

    def ats_formatting_task(self, agent: Agent, resume_content: str) -> Task:
        """
        Creates a task for the ATS & Formatting agent.

        Args:
            agent (Agent): The agent assigned to this task.
            resume_content (str): The text content of the resume.

        Returns:
            Task: A CrewAI task object.
        """
        return Task(
            description=dedent(f"""\
                Analyze the provided resume content for ATS compatibility and professional formatting.
                
                Resume Content:
                ---
                {resume_content}
                ---
            """),
            agent=agent,
            expected_output=self.__format_expected_output()
        )

    def projects_experience_task(self, agent: Agent, resume_content: str) -> Task:
        """
        Creates a task for the Projects & Experience agent.

        Args:
            agent (Agent): The agent assigned to this task.
            resume_content (str): The text content of the resume.

        Returns:
            Task: A CrewAI task object.
        """
        return Task(
            description=dedent(f"""\
                Evaluate the 'Projects' and 'Experience' sections of the resume.
                Focus on quantified impact, action verbs, and technical depth.

                Resume Content:
                ---
                {resume_content}
                ---
            """),
            agent=agent,
            expected_output=self.__format_expected_output()
        )

    def skills_assessment_task(self, agent: Agent, resume_content: str) -> Task:
        """
        Creates a task for the Skills Assessment agent.

        Args:
            agent (Agent): The agent assigned to this task.
            resume_content (str): The text content of the resume.

        Returns:
            Task: A CrewAI task object.
        """
        return Task(
            description=dedent(f"""\
                Assess the 'Skills' section for clarity, relevance, and organization.
                
                Resume Content:
                ---
                {resume_content}
                ---
            """),
            agent=agent,
            expected_output=self.__format_expected_output()
        )

    def tailoring_task(self, agent: Agent, resume_content: str, job_description: str) -> Task:
        """
        Creates a task for the Tailoring agent.

        Args:
            agent (Agent): The agent assigned to this task.
            resume_content (str): The text content of the resume.
            job_description (str): The job description to compare against.

        Returns:
            Task: A CrewAI task object.
        """
        return Task(
            description=dedent(f"""\
                Analyze the resume against the provided job description for tailoring.
                
                Resume Content:
                ---
                {resume_content}
                ---
                
                Job Description:
                ---
                {job_description}
                ---
            """),
            agent=agent,
            expected_output=self.__format_expected_output()
        )

    def digital_presence_task(self, agent: Agent, resume_content: str) -> Task:
        """
        Creates a task for the Digital Presence agent.

        Args:
            agent (Agent): The agent assigned to this task.
            resume_content (str): The text content of the resume.

        Returns:
            Task: A CrewAI task object.
        """
        return Task(
            description=dedent(f"""\
                Assess the candidate's professional online presence based on mentions of
                profiles like GitHub, LinkedIn, or personal portfolios in the resume.
                Do not attempt to access URLs.

                Resume Content:
                ---
                {resume_content}
                ---
            """),
            agent=agent,
            expected_output=self.__format_expected_output()
        )

    def content_quality_task(self, agent: Agent, resume_content: str) -> Task:
        """
        Creates a task for the Content Quality agent.

        Args:
            agent (Agent): The agent assigned to this task.
            resume_content (str): The text content of the resume.

        Returns:
            Task: A CrewAI task object.
        """
        return Task(
            description=dedent(f"""\
                Analyze the overall writing quality, checking for grammar, spelling,
                professional tone, and clarity.

                Resume Content:
                ---
                {resume_content}
                ---
            """),
            agent=agent,
            expected_output=self.__format_expected_output()
        )

    def education_task(self, agent: Agent, resume_content: str) -> Task:
        """
        Creates a task for the Education agent.

        Args:
            agent (Agent): The agent assigned to this task.
            resume_content (str): The text content of the resume.

        Returns:
            Task: A CrewAI task object.
        """
        return Task(
            description=dedent(f"""\
                Evaluate the 'Education' section for completeness, clarity, and proper formatting.

                Resume Content:
                ---
                {resume_content}
                ---
            """),
            agent=agent,
            expected_output=self.__format_expected_output()
        )
