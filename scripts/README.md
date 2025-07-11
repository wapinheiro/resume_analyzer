# Scripts Directory

This directory contains utility scripts for automating development, deployment, and maintenance tasks.

## Key Components:

-   `deployment.config.sh`: A centralized configuration file for all deployment variables (project IDs, service names, regions).
-   `deploy_all.sh`: A master script that orchestrates the deployment of all services by calling the other deployment scripts.
-   `deploy_backend.sh`: Script for deploying the FastAPI backend to Google Cloud Run.
-   `deploy_frontend.sh`: Script for deploying the React frontend to Firebase Hosting.
-   `destroy_all.sh`: A script to safely tear down all deployed cloud resources, useful for testing and cost management.
