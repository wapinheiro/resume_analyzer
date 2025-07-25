"""
ATS & Formatting Agent

This agent evaluates resumes for Applicant Tracking System (ATS) compatibility and professional formatting.
"""
from typing import List
from pydantic import BaseModel
from vertexai.generative_models import GenerativeModel
import os
from dotenv import load_dotenv
import json
import re

class AgentResponse(BaseModel):
    score: float
    feedback: List[str]
    suggestions: List[str]
    confidence: float


class ATSAgent:
    def __init__(self):
        load_dotenv()
        project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
        if not project_id:
            raise ValueError("GOOGLE_CLOUD_PROJECT environment variable not set.")
        self.model = GenerativeModel("gemini-2.5-flash")

    # Removed custom parser; now uses shared parser from utils.py

    def analyze(self, resume_text: str) -> AgentResponse:
        # Read shared and agent-specific prompt requirements
        shared_path = os.path.join(os.path.dirname(__file__), "prompt_requirements.md")
        agent_path = os.path.join(os.path.dirname(__file__), "ats_agent_prompt.md")
        with open(shared_path) as f:
            shared_reqs = f.read()
        with open(agent_path) as f:
            agent_reqs = f.read()
        prompt = f"""
{shared_reqs}\n\n{agent_reqs}\n\nResume:\n{resume_text}\n"""
        response = self.model.generate_content(prompt)
        from .utils import parse_gemini_llm_response
        parsed = parse_gemini_llm_response(response)
        if hasattr(parsed, 'dict'):
            return parsed.dict()
        return parsed
