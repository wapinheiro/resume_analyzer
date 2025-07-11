#!/bin/bash

# This script deploys the backend service to Google Cloud Run.
#
# PRE-REQUISITES:
# 1. This script is intended to be called from the master `deploy_all.sh` script.
# 2. `deployment.config.sh` must be sourced before running this script so that
#    GCP_PROJECT_ID, GCP_REGION, BACKEND_SERVICE_NAME, and DOCKER_IMAGE_NAME are
#    available as environment variables.

# Exit immediately if a command exits with a non-zero status.
set -e

echo "--- Building Docker Image ($DOCKER_IMAGE_NAME) ---"
# Build the Docker image and tag it for Google Container Registry (GCR)
docker build -t $DOCKER_IMAGE_NAME ../backend

echo "--- Pushing Image to Google Container Registry ---"
# Push the image to GCR
docker push $DOCKER_IMAGE_NAME

echo "--- Deploying to Cloud Run ---"
# Deploy the image to Cloud Run. All variables are sourced from the config file.
gcloud run deploy $BACKEND_SERVICE_NAME \
  --image $DOCKER_IMAGE_NAME \
  --platform managed \
  --region $GCP_REGION \
  --project $GCP_PROJECT_ID \
  --allow-unauthenticated # For public access, adjust as needed

echo "--- Backend Deployment Complete ---"
