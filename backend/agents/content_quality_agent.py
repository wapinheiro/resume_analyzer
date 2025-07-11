"""
File: content_quality_agent.py
Author: Wagner Pinheiro
Date: 2025-07-11
Last Modified: 2025-07-11

Purpose:
    This file defines the Content Quality Specialist agent. This agent is
    responsible for analyzing the overall writing quality of the resume,
    including grammar, spelling, tone, and clarity.

Dependencies:
    - crewai
    - langchain_google_vertexai
"""
from crewai import Agent
from langchain_google_vertexai import ChatVertexAI

# Initialize the LLM
llm = ChatVertexAI(model_name="gemini-1.5-flash-001", temperature=0.1)

# Define the weight for this agent's score
CONTENT_QUALITY_AGENT_WEIGHT = 0.05

content_quality_agent = Agent(
    role="Professional Writing and Content Editor",
    goal="""
    Analyze the overall writing quality of the resume, including the summary/objective section.
    Check for grammar, spelling, professional tone, clarity, and conciseness.
    Provide a score from 0-10, specific feedback, and actionable suggestions.
    """,
    backstory="""
    You are a meticulous editor with a background in technical and professional writing.
    You believe that clear and error-free communication is a reflection of a candidate's
    professionalism and attention to detail. You catch the small mistakes that others might
    miss and help refine the language to be as impactful as possible.
    """,
    llm=llm,
    verbose=True,
    allow_delegation=False,
    memory=False,
    max_iter=5,
)
