import os
import vertexai
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from vertexai.generative_models import GenerativeModel
from dotenv import load_dotenv
from agents.ats_agent import ATSAgent, AgentResponse
from agents.projects_agent import ProjectsAgent
from agents.skills_agent import SkillsAgent
from agents.tailoring_agent import TailoringAgent
from agents.digital_agent import DigitalAgent
from agents.content_agent import ContentAgent
from agents.education_agent import EducationAgent
from pydantic import BaseModel
from fastapi import Body
from agents.orchestrator import ResumeAnalysisCrew
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI(
    title="Resume Analyzer API",
    description="An API for analyzing resumes using a team of specialized AI agents.",
    version="0.1.0",
)

# Add CORS middleware to allow frontend requests from localhost:3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development, allow all. For production, restrict this.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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

@app.post("/v1/projects-agent", response_model=AgentResponse)
def run_projects_agent(input: ResumeInput = Body(...)):
    agent = ProjectsAgent()
    return agent.analyze(input.resume_text)

@app.post("/v1/skills-agent", response_model=AgentResponse)
def run_skills_agent(input: ResumeInput = Body(...)):
    agent = SkillsAgent()
    return agent.analyze(input.resume_text)

@app.post("/v1/tailoring-agent", response_model=AgentResponse)
def run_tailoring_agent(input: ResumeInput = Body(...)):
    agent = TailoringAgent()
    # For now, job_description is optional and empty
    return agent.analyze(input.resume_text, job_description="")

@app.post("/v1/digital-agent", response_model=AgentResponse)
def run_digital_agent(input: ResumeInput = Body(...)):
    agent = DigitalAgent()
    return agent.analyze(input.resume_text)

@app.post("/v1/content-agent", response_model=AgentResponse)
def run_content_agent(input: ResumeInput = Body(...)):
    agent = ContentAgent()
    return agent.analyze(input.resume_text)

@app.post("/v1/education-agent", response_model=AgentResponse)
def run_education_agent(input: ResumeInput = Body(...)):
    agent = EducationAgent()
    return agent.analyze(input.resume_text)

class OrchestratorInput(BaseModel):
    resume_text: str
    job_description: str = None

@app.post("/v1/analyze")
def analyze_resume(input: OrchestratorInput = Body(...)):
    crew = ResumeAnalysisCrew()
    results = crew.run(input.resume_text, input.job_description)
    return JSONResponse(content=results)
