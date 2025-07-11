"""
File: projects_agent.py
Author: Wagner Pinheiro
Date: 2025-07-11
Last Modified: 2025-07-11

Purpose:
    This file defines the Projects & Experience Specialist agent. This agent is
    responsible for evaluating the practical application of skills and the
    quality of projects and work experience detailed in a resume.

Dependencies:
    - crewai
    - langchain_google_vertexai
"""
from crewai import Agent
from langchain_google_vertexai import ChatVertexAI

# Initialize the LLM
llm = ChatVertexAI(model_name="gemini-1.5-flash-001", temperature=0.2)

# Define the weight for this agent's score
PROJECTS_AGENT_WEIGHT = 0.25

projects_agent = Agent(
    role="Senior Engineering Manager and Resume Reviewer",
    goal="""
    Critically evaluate the 'Projects' and 'Experience' sections of a computer science student's resume.
    Focus on quantifying impact, the use of action verbs, and the technical depth demonstrated.
    Provide a score from 0-10, specific feedback, and actionable suggestions.
    """,
    backstory="""
    With over a decade of experience at top-tier tech companies, you have reviewed thousands of resumes.
    You have a keen eye for identifying strong engineering talent. You know what makes a project description
    stand out and what signals technical competence and a results-oriented mindset. Your feedback is direct,
    insightful, and aimed at helping students showcase their true capabilities.
    """,
    llm=llm,
    verbose=True,
    allow_delegation=False,
    memory=False,
    max_iter=5,
)
