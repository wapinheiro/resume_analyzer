"""
File: schemas.py
Author: Wagner Pinheiro
Date: 2025-07-11
Last Modified: 2025-07-11

Purpose:
    This file defines the Pydantic data models (schemas) used for structuring
    the inputs and outputs of the AI agent analysis. These schemas ensure
    data consistency, validation, and clear API contracts.

Dependencies:
    - pydantic
"""
from pydantic import BaseModel, Field
from typing import List, Dict

class AgentResponse(BaseModel):
    """
    A standardized Pydantic model for agent responses, ensuring consistency
    and type safety in the data returned by each specialized agent.
    """
    score: float = Field(..., description="A 0-10 score for the analyzed category.")
    feedback: List[str] = Field(..., description="Specific, constructive feedback points based on the analysis.")
    suggestions: List[str] = Field(..., description="Actionable recommendations for improvement.")
    confidence: float = Field(..., description="The agent's confidence in its analysis, from 0.0 to 1.0.")

class OverallAnalysisResponse(BaseModel):
    """
    A Pydantic model to structure the final, aggregated analysis from all agents.
    """
    final_score: float = Field(..., description="The weighted final score from 0 to 100.")
    category_scores: Dict[str, float] = Field(..., description="A dictionary of scores from each agent category.")
    analysis_details: Dict[str, AgentResponse] = Field(..., description="Detailed responses from each individual agent.")
    summary: str = Field(..., description="A high-level summary of the resume's strengths and weaknesses.")
