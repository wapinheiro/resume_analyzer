# Development & Deployment Strategy: A Cloud-Ready Local Approach

This document outlines the hybrid strategy for developing and deploying the Resume Analyzer project. The primary goal is to enable rapid, cost-effective MVP development locally while ensuring the application is 100% ready for a seamless transition to a production cloud environment on Google Cloud Platform (GCP).

## Guiding Principles

1.  **Zero-Cost MVP Development**: Avoid incurring any cloud hosting costs during the initial development and buy-in phase. All development and demonstration will be done on a local machine.
2.  **High-Fidelity Production Mirror**: The local development environment must mirror the future production environment as closely as possible to de-risk the final deployment.
3.  **No Painful Migrations**: By preparing for the cloud from day one, we will avoid the complex and error-prone process of migrating a "local-only" project to a cloud-native architecture.
4.  **Professional & Credible Demo**: The MVP demo should not only showcase a working application but also demonstrate its technical readiness for a real-world launch.

## The Strategy: Develop Locally, Deploy with Confidence

### 1. Backend: Containerization with Docker

The FastAPI backend will be fully containerized using Docker.

-   **`backend/Dockerfile`**: This file defines the exact runtime environment for the application. It specifies the Python version, installs dependencies, and configures how the application server (Uvicorn) is run. This container image is the single, portable artifact that will be run locally and deployed to GCP Cloud Run.
-   **`backend/docker-compose.yml`**: This file orchestrates the local development environment. It defines and links two services:
    1.  **`api`**: Our FastAPI application, built from the `Dockerfile`.
    2.  **`chromadb`**: The ChromaDB vector database, using an official public image.
-   **Local Workflow**: A developer runs `docker-compose up --build` in the `backend` directory to start the entire backend stack. The API becomes available at `http://localhost:8000`.

### 2. Frontend: Standard Web Development

The React frontend is developed using standard Node.js tools.

-   **Local Workflow**: A developer runs `npm install` and `npm start` in the `frontend` directory. The development server starts the app on `http://localhost:3000`.
-   **Deployment Target**: The frontend is a static web application. It will be deployed to **Firebase Hosting**, which provides a global CDN, SSL, and a simple deployment process.

### 3. The Path to Production: A Single-Command Deployment

This strategy makes the final deployment incredibly simple and transparent after institutional buy-in is secured. The entire process is managed by a master script and a single configuration file.

1.  **Centralized Configuration (`scripts/deployment.config.sh`)**: This file is the single source of truth for all environment-specific settings. The university's technical staff will only need to edit this one file to input the official GCP and Firebase project IDs.

2.  **Master Deployment Script (`scripts/deploy_all.sh`)**: This script is the single command needed to launch the entire application. It automates every step:
    *   Loads the configuration.
    *   Builds the backend Docker image.
    *   Pushes the image to Google Container Registry.
    *   Deploys the backend to Cloud Run.
    *   Builds the frontend application.
    *   Deploys the frontend to Firebase Hosting.

3.  **The Three-Step Execution**: After receiving credentials, the launch process is:
    1.  **Configure**: Edit the `scripts/deployment.config.sh` file with the provided project IDs.
    2.  **Authenticate**: Log in to the `gcloud` and `firebase` command-line tools.
    3.  **Deploy**: Run the master script: `./scripts/deploy_all.sh`.

This approach ensures a rapid, reliable, and error-free launch, demonstrating a high level of professionalism and technical readiness.

### 4. Strategy Validation: The "Burner Project" Test

To guarantee that our single-command deployment works flawlessly, we validate it using a "Burner Project" testing strategy. This involves:
1.  Creating a temporary, disposable GCP project.
2.  Running the `deploy_all.sh` script to perform a live, end-to-end deployment.
3.  Verifying the live application.
4.  Running the `destroy_all.sh` script to completely and cleanly delete all test resources.

This validation step provides 100% confidence in our deployment automation before it's used in the official university environment. For full details, see the `TESTING_STRATEGY.md` document.
