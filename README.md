# Resume Analyzer

An intelligent web application designed specifically for BYU Computer Science students to upload, analyze, and receive detailed feedback on their resumes. The system uses specialized AI agents to provide comprehensive scoring and actionable recommendations based on industry best practices and research-backed criteria.

## 🎯 Project Overview

The Resume Analyzer addresses the critical need for CS students to create compelling resumes that can successfully navigate both Applicant Tracking Systems (ATS) and human recruiters. By leveraging specialized AI agents, the system provides detailed analysis across seven key categories with specific, actionable feedback.

## 🏗️ Project Structure

The project should be organized as follows:

```
byu/                # Organization-level directory
└── resume_analyzer/ # Project-level directory
    ├── backend/     # Backend code and virtual environment
    │   ├── main.py
    │   ├── requirements.txt
    │   └── venv/
    ├── docs/        # Documentation
    ├── .env         # Environment variables
    ├── README.md    # Project overview
    └── ...          # Other project files
```

- All backend code and dependencies must reside in `resume_analyzer/backend/`.
- The only virtual environment should be `resume_analyzer/backend/venv/`.
- No code or venvs should exist at the organization level (`byu/`).

If you find stray folders or files at the organization level, delete them to keep the project clean.

## 🛠️ Core Technology

-   **Backend:** Python
-   **Cloud Provider:** Google Cloud Platform (GCP)
-   **AI/ML:** Google Cloud Vertex AI (Gemini Models)

## 🚀 Getting Started

To get started with the backend service, please refer to the detailed instructions in the `backend/README.md` file.

---

*The following sections contain more detailed architectural and technical plans.*

### Key Features

- **📄 Resume Upload & Processing**: Support for PDF resume uploads with intelligent text extraction
- **🤖 AI-Powered Analysis**: Specialized agents for different aspects of resume evaluation
- **📊 Comprehensive Scoring**: Weighted scoring system across 7 critical categories
- **💡 Detailed Feedback**: Specific, actionable recommendations for improvement
- **🎯 BYU CS Focus**: Tailored specifically for Computer Science students and industry expectations
- **📈 Continuous Learning**: Agents improve over time through usage and feedback

## 🏗️ System Architecture

The Resume Analyzer uses an **agent-based architecture** where specialized AI agents handle different aspects of resume analysis:

### Specialized Agents
1. **ATS & Formatting Agent** (20% weight) - Structure, formatting, ATS compatibility
2. **Projects & Experience Agent** (25% weight) - Project quality, quantification, impact
3. **Skills Assessment Agent** (15% weight) - Technical and soft skills evaluation
4. **Tailoring Agent** (20% weight) - Job description alignment and customization
5. **Digital Footprint Agent** (10% weight) - GitHub, LinkedIn, online presence
6. **Content Quality Agent** (5% weight) - Summary/objective analysis
7. **Education Validation Agent** (5% weight) - Education section completeness

## 🛠️ Tech Stack

### Backend
- **Python 3.11+** - Core backend language
- **FastAPI** - Modern, high-performance web framework
- **CrewAI** - Multi-agent orchestration and management
- **PostgreSQL** - Database for analysis results and training data
- **PyPDF2/pdfplumber** - PDF text extraction
- **Google Gemini 1.5 Flash** - Primary LLM for agent intelligence
- **OpenAI GPT-4** & **Anthropic Claude** - Secondary LLMs for specialized tasks

### Frontend
- **React 18** - Modern frontend framework
- **TypeScript** - Type-safe development
- **Tailwind CSS** - Utility-first styling
- **React Query** - Server state management

### Infrastructure
- **Docker & Docker Compose** - For containerization and local development orchestration.
- **Google Cloud Platform (GCP)** - Target cloud for production deployment.
  - **Cloud Run** - Serverless backend hosting.
  - **Firebase Hosting** - Frontend hosting with a global CDN.
  - **Vertex AI** - For scalable access to Google Gemini models.
- **GitHub Actions** - CI/CD pipeline.

## 🚀 Local Development Setup

This project uses a "Cloud-Ready Local" approach. The entire application stack can be run locally, configured for a seamless deployment to the cloud.

### Prerequisites

Before you begin, ensure you have the following tools installed:

- **Docker & Docker Compose**: Required to run the containerized backend services.
  - [Install Docker Desktop](https://docs.docker.com/get-docker/) (includes Docker Compose).
- **Node.js & npm**: Required for the React frontend. `npm` is included with Node.js.
  - [Install Node.js v18+ and npm](https://nodejs.org/en/download/).
- **Git**: For cloning the repository.
  - [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
- **Google Cloud CLI**: Required for interacting with Google Cloud services.
  - [Install Google Cloud CLI](https://cloud.google.com/sdk/docs/install) for your operating system.

### Environment Configuration

The AI agents require API keys to function.

1.  **Create an environment file:**
    In the `backend` directory, create a file named `.env`.
    ```sh
    touch backend/.env
    ```

2.  **Add your API keys:**
    Open the `backend/.env` file and add your API keys. For example:
    ```env
    # backend/.env
    GOOGLE_API_KEY="your_google_api_key_here"
    SERPER_API_KEY="your_serper_api_key_here"
    ```
    > **Note**: These keys are passed securely to the Docker container by the `docker-compose.yml` file and are not exposed publicly.

### Local Development

1.  **Install Google Cloud CLI:**
    Follow the official documentation to [install the Google Cloud CLI](https://cloud.google.com/sdk/docs/install) for your operating system.

2.  **Authenticate with Google Cloud:**
    After installing the CLI, you need to authenticate your local environment to access Google Cloud services. Run the following command in your terminal and follow the prompts:
    ```bash
    gcloud auth application-default login
    ```

3.  **Set up the backend virtual environment:**
    ```bash
    cd backend
    python -m venv venv
    source venv/bin/activate
    ```

4.  **Run the backend server:**
    ```bash
    uvicorn main:app --reload
    ```

5.  **Run the validation script:**
    In a separate terminal, set up the validation environment and run the script to test the backend.
    ```bash
    cd backend
    source venv/bin/activate
    python -m scripts.validate_backend
    ```

6.  **Start the frontend development server:**
    In another terminal, start the React frontend.
    ```bash
    cd frontend
    npm start
    ```

## ☁️ Deployment

The application is designed for a simple, single-command deployment to GCP and Firebase.

### The "Configure, Authenticate, Deploy" Model

1.  **Configure**: Open `scripts/deployment.config.sh` and fill in the placeholder values for your institutional GCP and Firebase project IDs.
2.  **Authenticate**: Log in to the Google Cloud and Firebase CLIs:
    ```bash
    gcloud auth login
    firebase login
    ```
3.  **Deploy**: Run the master deployment script from the `scripts` directory:
    ```bash
    ./deploy_all.sh
    ```

This process handles the entire build and deployment for both the backend and frontend, making the launch process rapid and reliable.

## 📋 Usage

1. **Upload Resume**: Students upload their PDF resume
2. **Analysis**: The system processes the resume through specialized agents
3. **Scoring**: Receive scores across 7 categories (0-10 scale)
4. **Feedback**: Get detailed, actionable recommendations
5. **Improvement**: Iterate and re-analyze for better scores

## 📊 Scoring Methodology

The system uses a research-backed scoring methodology with weighted categories:

| Category | Weight | Focus Area |
|----------|--------|------------|
| ATS & Formatting | 20% | Structure, layout, ATS compatibility |
| Projects & Experience | 25% | Practical application, quantification |
| Tailoring & Customization | 20% | Job-specific optimization |
| Skills | 15% | Technical and soft skills assessment |
| Digital Footprint | 10% | Online presence validation |
| Summary/Objective | 5% | Introduction quality |
| Education & Certifications | 5% | Academic credentials |

**Overall Score** = Weighted average of all categories (0-100 scale)

## 🤝 Contributing

We welcome contributions from the BYU CS community! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Process
1. Fork the repository
2. Create a feature branch
3. Make changes with tests
4. Submit a pull request

## 📚 Documentation

- [Architecture Overview](docs/ARCHITECTURE.md)
- [API Documentation](docs/API_DOCUMENTATION.md)
- [Agent Specifications](docs/AGENT_SPECIFICATIONS.md)
- [Scoring Methodology](docs/SCORING_METHODOLOGY.md)
- [Development Setup](docs/DEVELOPMENT_SETUP.md)
- [User Guide](docs/USER_GUIDE.md)

## 🔒 Privacy & Security

- Resume data is processed securely and not stored permanently
- All analysis is performed locally/privately
- No personal information is shared with third parties
- Students maintain full control over their data

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🏫 About

Developed for BYU Computer Science students to bridge the gap between academic learning and industry expectations. Based on comprehensive research of modern hiring practices and resume best practices in the tech industry.

## 📞 Support

- **Issues**: Report bugs via GitHub Issues
- **Questions**: Contact Wagner Pinheiro at wagner@cs.byu.edu
- **Feature Requests**: Submit via GitHub Discussions

---

**Made with ❤️ for BYU CS Students**

## ✅ Integration Milestone: FastAPI + Gemini 2.5

- The `/v1/test-gemini` endpoint is live and successfully connects to Gemini 2.5 Flash via Vertex AI.
- The backend is now always running and ready for incremental agent integration.
- See the [work diary](docs/project_plan/WORK_DIARY.md) for a detailed log of this milestone.
