#!/bin/bash

# -----------------------------------------------------------------------------
# DEPLOYMENT CONFIGURATION
# -----------------------------------------------------------------------------
# Instructions:
# 1. Fill in the placeholder values below with your institutional credentials
#    once they are provided.
# 2. This file centralizes all environment-specific variables for easy management.
# 3. In a real-world scenario with sensitive keys, this file would be
#    added to .gitignore and managed securely. For this project, placeholders
#    are used.
# -----------------------------------------------------------------------------

# --- Google Cloud Platform (GCP) Configuration ---
# The unique ID for your GCP project.
export GCP_PROJECT_ID="byu-cs-resume-analyzer"

# The GCP region where services will be deployed (e.g., us-central1, us-west1).
export GCP_REGION="us-central1"

# The name for the backend Cloud Run service.
export BACKEND_SERVICE_NAME="resume-analyzer-api"


# --- Firebase Configuration ---
# The unique ID for your Firebase project. This should match your GCP Project ID
# if they are linked, which is the recommended setup.
export FIREBASE_PROJECT_ID="byu-cs-resume-analyzer"


# --- Docker Image Configuration ---
# The name of the container image for the backend.
# This will be tagged and pushed to Google Container Registry (GCR).
# Format: gcr.io/PROJECT_ID/SERVICE_NAME
export DOCKER_IMAGE_NAME="gcr.io/$GCP_PROJECT_ID/$BACKEND_SERVICE_NAME"
