"""
File: main.py
Author: Wagner Pinheiro
Date: 2025-07-11
Last Modified: 2025-07-11

Purpose:
    This script serves as the main entry point for the Resume Analyzer FastAPI backend.
    It defines API endpoints for health checks and for receiving resume analysis requests.
    It handles PDF uploads, extracts text content, and invokes the agent crew for analysis.

Dependencies:
    - fastapi
    - pydantic
    - python-multipart
    - PyMuPDF
    - agents.crew
    - agents.schemas
"""

import fitz  # PyMuPDF
from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from pydantic import BaseModel, Field
from typing import Optional

from .agents.crew import run_resume_analysis
from .agents.schemas import OverallAnalysisResponse

app = FastAPI(
    title="Resume Analyzer API",
    description="An API for analyzing resumes using a team of specialized AI agents.",
    version="0.1.0",
)

@app.get("/", tags=["Health Check"])
async def read_root():
    """
    Root endpoint for health check.

    Returns:
        dict: A message indicating the API is running.
    """
    return {"message": "Resume Analyzer API is running"}

@app.post("/analyze", response_model=OverallAnalysisResponse, tags=["Analysis"])
async def analyze_resume(
    job_description: str = Form(..., description="The job description to tailor the resume against."),
    resume_file: UploadFile = File(..., description="The resume file (PDF) to be analyzed.")
):
    """
    Analyzes a resume against a job description.

    This endpoint accepts a PDF resume and a job description, extracts the text
    from the PDF, and then uses the AI agent crew to perform a detailed analysis.

    Args:
        job_description (str): The job description for tailoring analysis.
        resume_file (UploadFile): The user's resume in PDF format.

    Returns:
        OverallAnalysisResponse: A JSON object containing the detailed analysis,
                                 scores, and feedback from the agent crew.
    
    Raises:
        HTTPException: If the uploaded file is not a PDF or if text extraction fails.
    """
    if resume_file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a PDF.")

    try:
        # Read the PDF content from the uploaded file
        pdf_bytes = await resume_file.read()
        pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
        
        resume_content = ""
        for page in pdf_document:
            resume_content += page.get_text()
        
        pdf_document.close()

        if not resume_content.strip():
            raise HTTPException(status_code=422, detail="Could not extract text from the PDF.")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process PDF file: {str(e)}")

    try:
        # Run the analysis using the agent crew
        analysis_result = run_resume_analysis(
            resume_content=resume_content,
            job_description=job_description
        )
        return analysis_result
    except Exception as e:
        # Catch potential errors from the analysis crew
        raise HTTPException(status_code=500, detail=f"An error occurred during analysis: {str(e)}")
