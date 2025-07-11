#!/bin/bash

# This script deploys the frontend application to Firebase Hosting.
#
# PRE-REQUISITES:
# 1. This script is intended to be called from the master `deploy_all.sh` script.
# 2. `deployment.config.sh` must be sourced so that FIREBASE_PROJECT_ID is available.
# 3. Node.js and npm are installed.
# 4. Firebase CLI is installed and authenticated.

# Exit immediately if a command exits with a non-zero status.
set -e

echo "--- Building React App for Production ---"
# Navigate to the frontend directory
cd ../frontend

# Install dependencies if they are not already installed
npm install

# Build the static files
npm run build

echo "--- Deploying to Firebase Hosting (Project: $FIREBASE_PROJECT_ID) ---"
# Deploy to Firebase. The --project flag ensures we deploy to the correct project
# as defined in the config file.
firebase deploy --only hosting --project $FIREBASE_PROJECT_ID

echo "--- Frontend Deployment Complete ---"
