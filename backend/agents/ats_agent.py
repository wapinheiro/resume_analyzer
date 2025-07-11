"""
File: ats_agent.py
Author: Wagner Pinheiro
Date: 2025-07-11
Last Modified: 2025-07-11

Purpose:
    This file defines the ATS & Formatting Specialist agent for the resume analysis crew.
    This agent is responsible for analyzing a resume's compatibility with Applicant
    Tracking Systems (ATS) and its overall professional formatting.

Dependencies:
    - crewai
    - langchain_google_vertexai
"""
from crewai import Agent
from langchain_google_vertexai import ChatVertexAI

# Initialize the LLM for all agents in this module
# Using a shared instance can be slightly more efficient
llm = ChatVertexAI(model_name="gemini-1.5-flash-001", temperature=0.1)

# Define the weight for this agent's score
ATS_AGENT_WEIGHT = 0.20

ats_agent = Agent(
    role="Resume ATS and Formatting Specialist",
    goal=f"""
    Analyze a resume to determine its compatibility with Applicant Tracking Systems (ATS)
    and evaluate its overall formatting.
    Provide a score from 0-10, specific feedback, and actionable suggestions based
    on the analysis.
    """,
    backstory="""
    As an expert in resume parsing technologies and professional document standards,
    you are skilled at identifying subtle issues that cause resumes to be rejected by
    automated systems. You ensure that every resume is not only machine-readable but
    also visually appealing and professional to human recruiters.
    """,
    llm=llm,
    verbose=True,
    allow_delegation=False,
    memory=False,
    max_iter=5,
)
