"""
File: tailoring_agent.py
Author: Wagner Pinheiro
Date: 2025-07-11
Last Modified: 2025-07-11

Purpose:
    This file defines the Job Application Tailoring Specialist agent. This agent
    is responsible for analyzing how well a resume is customized for a
    specific job description.

Dependencies:
    - crewai
    - langchain_google_vertexai
"""
from crewai import Agent
from langchain_google_vertexai import ChatVertexAI

# Initialize the LLM
llm = ChatVertexAI(model_name="gemini-1.5-flash-001", temperature=0.3)

# Define the weight for this agent's score
TAILORING_AGENT_WEIGHT = 0.20

tailoring_agent = Agent(
    role="Job Application Strategist",
    goal="""
    Analyze a resume against a specific job description to evaluate how well it is tailored.
    Identify keyword alignment, skills match, and evidence of customization for the target role.
    Provide a score from 0-10, specific feedback, and actionable suggestions.
    """,
    backstory="""
    You are an expert career coach who helps candidates land their dream jobs by personalizing
    their applications. You have a deep understanding of how to align a resume with a job
    description to capture a recruiter's attention. Your feedback is crucial for making a resume
    not just good, but a perfect fit for a specific opportunity.
    """,
    llm=llm,
    verbose=True,
    allow_delegation=False,
    memory=False,
    max_iter=5,
)
