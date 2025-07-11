"""
File: skills_agent.py
Author: Wagner Pinheiro
Date: 2025-07-11
Last Modified: 2025-07-11

Purpose:
    This file defines the Skills Assessment Specialist agent. This agent is
    responsible for evaluating the presentation and relevance of technical
    and soft skills listed on a resume.

Dependencies:
    - crewai
    - langchain_google_vertexai
"""
from crewai import Agent
from langchain_google_vertexai import ChatVertexAI

# Initialize the LLM
llm = ChatVertexAI(model_name="gemini-1.5-flash-001", temperature=0.1)

# Define the weight for this agent's score
SKILLS_AGENT_WEIGHT = 0.15

skills_agent = Agent(
    role="Technical Recruiter and Skills Analyst",
    goal="""
    Assess the 'Skills' section of a resume for clarity, relevance, and organization.
    Evaluate the mix of technical (programming languages, frameworks, tools) and soft skills.
    Provide a score from 0-10, specific feedback, and actionable suggestions.
    """,
    backstory="""
    You are a seasoned technical recruiter who specializes in the tech industry. You understand
    what skills are in high demand and how they should be presented on a resume. You can quickly
    determine if a candidate's skill set aligns with modern industry standards and best practices.
    Your goal is to help students present their skills in the most effective way possible.
    """,
    llm=llm,
    verbose=True,
    allow_delegation=False,
    memory=False,
    max_iter=5,
)
