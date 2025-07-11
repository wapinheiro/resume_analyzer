"""
File: digital_presence_agent.py
Author: Wagner Pinheiro
Date: 2025-07-11
Last Modified: 2025-07-11

Purpose:
    This file defines the Digital Presence Analyst agent. This agent is
    responsible for assessing the candidate's professional online presence
    based on links and mentions in the resume (e.g., GitHub, LinkedIn).

Dependencies:
    - crewai
    - langchain_google_vertexai
"""
from crewai import Agent
from langchain_google_vertexai import ChatVertexAI

# Initialize the LLM
llm = ChatVertexAI(model_name="gemini-1.5-flash-001", temperature=0.1)

# Define the weight for this agent's score
DIGITAL_PRESENCE_AGENT_WEIGHT = 0.10

digital_presence_agent = Agent(
    role="Digital Footprint Analyst",
    goal="""
    Assess the candidate's professional online presence based on links provided in the resume (e.g., GitHub, LinkedIn, Portfolio).
    Evaluate the quality, completeness, and activity of these profiles based on how they are presented in the resume.
    Provide a score from 0-10, specific feedback, and actionable suggestions.
    """,
    backstory="""
    You are a specialist in online branding and professional networking. You understand how recruiters
    use online profiles to vet candidates. You can analyze a GitHub profile for meaningful activity,
    a LinkedIn profile for professionalism and consistency, and a personal portfolio for its effectiveness
    in showcasing projects and skills. You will not actually visit the URLs, but you will analyze the resume content for mentions of these profiles and how they are presented.
    """,
    llm=llm,
    verbose=True,
    allow_delegation=False,
    memory=False,
    max_iter=5,
)
