#!/bin/bash

# =============================================================================
# MASTER DEPLOYMENT SCRIPT
# =============================================================================
# This script orchestrates the entire deployment process for the Resume Analyzer.
# It sources configuration from `deployment.config.sh` and then executes the
# backend and frontend deployment scripts in sequence.
#
# USAGE:
# 1. Ensure you have authenticated with Google Cloud (`gcloud auth login`) and
#    Firebase (`firebase login`).
# 2. Ensure you have the necessary IAM permissions for the target projects.
# 3. Run this script from the `scripts` directory:
#    ./deploy_all.sh
# =============================================================================

# Exit immediately if a command exits with a non-zero status.
set -e

# --- 1. Load Configuration ---
echo "▶️ Loading deployment configuration..."
source deployment.config.sh
echo "✅ Configuration loaded for GCP Project: $GCP_PROJECT_ID"
echo ""

# --- 2. Deploy Backend ---
echo "▶️ Starting backend deployment..."
./deploy_backend.sh
echo "✅ Backend deployment script finished."
echo ""

# --- 3. Deploy Frontend ---
echo "▶️ Starting frontend deployment..."
./deploy_frontend.sh
echo "✅ Frontend deployment script finished."
echo ""

# --- 4. Final Summary ---
echo "🚀 DEPLOYMENT COMPLETE! 🚀"
echo "--------------------------------------------------"
echo "Backend Service ($BACKEND_SERVICE_NAME) URL:"
# The gcloud command can be slow, so we construct the URL manually for speed.
# The actual URL will be printed at the end of the deploy_backend.sh script.
echo "   https://$BACKEND_SERVICE_NAME-*.run.app (Check terminal output for exact URL)"
echo ""
echo "Frontend Application URL:"
echo "   https://$FIREBASE_PROJECT_ID.web.app"
echo "   https://$FIREBASE_PROJECT_ID.firebaseapp.com"
echo "--------------------------------------------------"
