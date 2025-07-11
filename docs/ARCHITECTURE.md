# System Architecture

## Overview

The Resume Analyzer employs a sophisticated **agent-based architecture** that leverages specialized AI agents to analyze different aspects of a resume. This modular approach ensures focused expertise, scalability, and continuous improvement through specialized learning.

## 🏗️ High-Level Architecture

```text
┌───────────────────────────────┐      ┌──────────────────────────┐
│  React Frontend               │      │  FastAPI Backend         │
│  (Firebase Hosting)           │◄────►│  (Cloud Run)             │
└───────────────────────────────┘      └────────────┬─────────────┘
                                                    │
                                                    ▼
                                     ┌──────────────────────────┐
                                     │      Agent Orchestra     │
                                     │         (CrewAI)         │
                                     └────────────┬─────────────┘
                                                    │
                                                    ▼
                       ┌──────────────────────────────────────────────┐
                       │              Specialized Agents              │
                       ├──────────────────────────────────────────────┤
                       │ ATS Agent │ Projects │ Skills │ Tailoring    │
                       │ (20%)     │ Agent    │ Agent  │ Agent (20%)  │
                       │           │ (25%)    │ (15%)  │              │
                       ├───────────┼──────────┼────────┼──────────────┤
                       │ Digital   │ Content  │ Education            │
                       │ Agent     │ Agent    │ Agent  │ Agent (5%)   │
                       │ (10%)     │ (5%)     │                      │
                       └────────────┬───────────────────────────────┘
                                    │
                                    ▼
                         ┌──────────────────────────┐
                         │   Google Cloud AI        │
                         │       (Vertex AI)        │
                         │   - Gemini 1.5 Flash     │
                         └──────────────────────────┘
```

## 🎯 Agent-Based Design Philosophy

### Core Principles
1.  **Specialization**: Each agent focuses on a specific domain of resume analysis.
2.  **Modularity**: Agents can be developed, tested, and improved independently.
3.  **Scalability**: New agents can be added without affecting existing ones.
4.  **Parallel Processing**: Multiple agents can analyze simultaneously for speed.
5.  **Explainable AI**: Each agent provides specific, targeted feedback, making the final score transparent.

### Agent Communication Protocol
```python
# Pydantic model for a standardized agent response
class AgentResponse(BaseModel):
    score: float          # 0-10 score for this category
    feedback: List[str]   # Specific feedback points
    suggestions: List[str] # Actionable recommendations
    confidence: float     # Agent's confidence in its analysis
```

## 🤖 Specialized Agents

### 1. ATS & Formatting Agent (Weight: 20%)
-   **Responsibility**: Ensures resume can pass Applicant Tracking Systems and has professional formatting.
-   **Analysis Focus**: File format, font consistency, section structure, keyword density.

### 2. Projects & Experience Agent (Weight: 25%)
-   **Responsibility**: Evaluates the practical application of skills and the quality of projects.
-   **Analysis Focus**: Impact metrics (quantification), action verb usage, technical complexity.

### 3. Skills Assessment Agent (Weight: 15%)
-   **Responsibility**: Evaluates the presentation of technical and soft skills.
-   **Analysis Focus**: Skill categorization, relevance to industry trends, soft skill integration.

### 4. Tailoring Agent (Weight: 20%)
-   **Responsibility**: Analyzes how well the resume is customized for a specific job description.
-   **Analysis Focus**: Keyword matching, role-specific optimization, evidence of customization.

### 5. Digital Footprint Agent (Weight: 10%)
-   **Responsibility**: Validates and scores the candidate's online professional presence.
-   **Analysis Focus**: GitHub profile activity, LinkedIn consistency, portfolio quality.

### 6. Content Quality Agent (Weight: 5%)
-   **Responsibility**: Analyzes the summary/objective and overall writing quality.
-   **Analysis Focus**: Grammar, professional tone, clarity, and conciseness.

### 7. Education Validation Agent (Weight: 5%)
-   **Responsibility**: Scores the education section for completeness and relevance.
-   **Analysis Focus**: Degree information, GPA presentation, relevant coursework.

## 🔄 Agent Orchestration Workflow

The analysis is managed by a **Crew** from the CrewAI framework.

```python
# Simplified orchestration logic
class ResumeAnalysisCrew:
    def run(self, resume_content: str, job_description: str):
        # Define Agents (ATS, Projects, etc.)
        ats_agent = Agent(...)
        projects_agent = Agent(...)

        # Define Tasks for each agent
        ats_task = Task(description="Analyze ATS compatibility...", agent=ats_agent)
        projects_task = Task(description="Evaluate projects...", agent=projects_agent)

        # Form the Crew and kick off the process
        resume_crew = Crew(
            agents=[ats_agent, projects_agent],
            tasks=[ats_task, projects_task],
            process=Process.sequential # Can be parallel for performance
        )
        
        result = resume_crew.kickoff()
        return result
```

## 🧠 Learning and Improvement

-   **Feedback Loop**: User feedback on the quality of suggestions will be used to refine agent prompts and logic.
-   **A/B Testing**: We can deploy two versions of an agent's prompt or logic and use Vertex AI Experiments to see which performs better against our internal scoring rubric.
-   **Domain Adaptation**: By analyzing anonymized, high-scoring resumes, agents can learn to identify successful patterns.

## 🔐 Security and Privacy

-   **Data Handling**: Resume data is processed in-memory on Cloud Run and is not stored permanently.
-   **Agent Security**: We will implement input validation and sanitization on all data passed to the agents to prevent prompt injection.
-   **API Key Management**: All API keys for external services (like Serper.dev or OpenAI) will be stored securely in Google Secret Manager.
-   **Anonymization**: Any data stored for analytics will be fully anonymized, with all personally identifiable information (PII) removed.

## ☁️ Development and Deployment Flow

This project follows a **"Cloud-Ready Local"** development model. This strategy allows for zero-cost local development while ensuring the application is primed for a seamless, one-step deployment to a production cloud environment.

### 1. Local Development Environment
-   **Orchestration**: The entire backend, including the API server and the ChromaDB vector database, is orchestrated locally using **Docker Compose**.
-   **Backend**: The FastAPI application is containerized with **Docker**. This guarantees that the development environment is identical to the production environment.
-   **Frontend**: The React application is run using a standard Node.js development server (`npm start`).

### 2. Deployment to Production
The deployment process is automated via a single master script.
-   **Backend**: A pre-written script (`scripts/deploy_backend.sh`) deploys the backend container to **GCP Cloud Run**.
-   **Frontend**: A pre-written script (`scripts/deploy_frontend.sh`) builds and deploys the static frontend assets to **Firebase Hosting**.

### 3. Strategy Validation: The "Burner Project" Test
To guarantee that our single-command deployment works flawlessly, we validate it using a "Burner Project" testing strategy. This involves:
1.  Creating a temporary, disposable GCP project.
2.  Running the `deploy_all.sh` script to perform a live, end-to-end deployment.
3.  Verifying the live application.
4.  Running the `destroy_all.sh` script to completely and cleanly delete all test resources.

This validation step provides 100% confidence in our deployment automation. For full details, see the `TESTING_STRATEGY.md` document.
