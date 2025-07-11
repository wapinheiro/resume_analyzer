"""
File: education_agent.py
Author: Wagner Pinheiro
Date: 2025-07-11
Last Modified: 2025-07-11

Purpose:
    This file defines the Education Validation Specialist agent. This agent is
    responsible for scoring the education section of a resume for
    completeness, relevance, and professional formatting.

Dependencies:
    - crewai
    - langchain_google_vertexai
"""
from crewai import Agent
from langchain_google_vertexai import ChatVertexAI

# Initialize the LLM
llm = ChatVertexAI(model_name="gemini-1.5-flash-001", temperature=0.1)

# Define the weight for this agent's score
EDUCATION_AGENT_WEIGHT = 0.05

education_agent = Agent(
    role="University Academic Advisor and Career Counselor",
    goal="""
    Evaluate the 'Education' section of a resume for completeness, clarity, and best practices.
    Check for proper formatting of degree, university, graduation date, GPA, and relevant coursework.
    Provide a score from 0-10, specific feedback, and actionable suggestions.
    """,
    backstory="""
    As a seasoned academic advisor, you have guided countless students in presenting their
    educational backgrounds effectively on their resumes. You know the standard conventions
    and what recruiters expect to see. Your focus is on ensuring this section is clear,
    professional, and accurately reflects the student's academic achievements.
    """,
    llm=llm,
    verbose=True,
    allow_delegation=False,
    memory=False,
    max_iter=5,
)
