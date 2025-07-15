"""
ATS & Formatting Agent

This agent evaluates resumes for Applicant Tracking System (ATS) compatibility and professional formatting.
"""
from typing import List
from pydantic import BaseModel
from vertexai.generative_models import GenerativeModel
import os
from dotenv import load_dotenv

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

    def analyze(self, resume_text: str) -> AgentResponse:
        prompt = f"""
        You are an ATS & Formatting Agent. Analyze the following resume for:
        - File format and structure
        - Font consistency
        - Section structure
        - Keyword density
        Provide a score (0-10), specific feedback, actionable suggestions, and your confidence (0-1).
        Resume:
        {resume_text}
        Respond in JSON with keys: score, feedback, suggestions, confidence.
        """
        response = self.model.generate_content(prompt)
        # For now, return a dummy response for validation
        return AgentResponse(
            score=8.5,
            feedback=["Good section structure.", "Font is consistent."],
            suggestions=["Increase keyword density for ATS."],
            confidence=0.9
        )
