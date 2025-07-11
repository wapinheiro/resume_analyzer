# Resume Analyzer

An intelligent web application designed specifically for BYU Computer Science students to upload, analyze, and receive detailed feedback on their resumes. The system uses specialized AI agents to provide comprehensive scoring and actionable recommendations based on industry best practices and research-backed criteria.

## 🎯 Project Overview

The Resume Analyzer addresses the critical need for CS students to create compelling resumes that can successfully navigate both Applicant Tracking Systems (ATS) and human recruiters. By leveraging specialized AI agents, the system provides detailed analysis across seven key categories with specific, actionable feedback.

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

This project uses a "Cloud-Ready Local" approach. The entire application stack can be run locally using Docker Compose and NPM, while being configured for a seamless deployment to Google Cloud.

### Prerequisites
- **Docker Desktop**: [Install Docker](https://docs.docker.com/get-docker/)
- **Node.js v18+**: [Install Node.js](https://nodejs.org/)

### Running the Application

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/resume-analyzer.git
    cd resume-analyzer
    ```

2.  **Start the Backend (API & Database):**
    The backend, including the ChromaDB vector store, is managed by Docker Compose.
    ```bash
    cd backend
    docker-compose up --build
    ```
    The API will be available at `http://localhost:8000`.

3.  **Start the Frontend:**
    In a separate terminal, start the React development server.
    ```bash
    cd frontend
    npm install
    npm start
    ```
    The frontend will be available at `http://localhost:3000`.

4.  **Access the Application:**
    Open your web browser to `http://localhost:3000` to use the application.

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
