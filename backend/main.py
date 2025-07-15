import os
import vertexai
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from vertexai.generative_models import GenerativeModel
from dotenv import load_dotenv
from agents.ats_agent import ATSAgent, AgentResponse
from pydantic import BaseModel
from fastapi import Body

# Initialize FastAPI app
app = FastAPI(
    title="Resume Analyzer API",
    description="An API for analyzing resumes using a team of specialized AI agents.",
    version="0.1.0",
)

@app.get("/")
def root():
    """
    Root endpoint for the API.
    Returns a welcome message.
    """
    return {"status": "ok", "message": "Resume Analyzer API is running."}

@app.get("/v1/test-gemini")
def test_gemini_endpoint():
    """
    Tests the connection to Google's Gemini model via Vertex AI.
    Returns a success message if the connection is established.

    This function initializes the Vertex AI SDK and attempts to interact with
    the 'gemini-2.5-flash' model. It confirms that the connection is successful
    and prints a confirmation message.
    """
    try:
        # Load environment variables from a .env file
        load_dotenv()
        project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
        if not project_id:
            raise ValueError("GOOGLE_CLOUD_PROJECT environment variable not set.")
        vertexai.init(project=project_id, location="us-central1")
        model = GenerativeModel("gemini-2.5-flash")
        response = model.generate_content("test")
        return {"success": True, "message": "Successfully connected to Gemini 2.5 Flash.", "response": str(response)}
    except Exception as e:
        return JSONResponse(status_code=500, content={"success": False, "error": str(e)})

class ResumeInput(BaseModel):
    resume_text: str

@app.post("/v1/ats-agent", response_model=AgentResponse)
def run_ats_agent(input: ResumeInput = Body(...)):
    agent = ATSAgent()
    return agent.analyze(input.resume_text)
