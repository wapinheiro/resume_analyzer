#!/bin/bash

# =============================================================================
# SELF-DESTRUCT SCRIPT FOR BURNER PROJECT
# =============================================================================
# This script completely deletes the GCP project specified in the deployment
# configuration. It is the "self-destruct button" for the burner project
# used in our testing strategy.
#
# WARNING: This action is irreversible. It will permanently delete the project
# and all resources within it.
#
# USAGE:
# 1. Ensure you are in the `scripts` directory.
# 2. Run the script: ./destroy_all.sh
# =============================================================================

# Exit immediately if a command exits with a non-zero status.
set -e

# --- 1. Load Configuration ---
echo "▶️ Loading deployment configuration to identify target project..."
source deployment.config.sh
echo "✅ Configuration loaded."
echo ""

# --- 2. Confirmation Prompt ---
echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
echo "!! WARNING: YOU ARE ABOUT TO PERMANENTLY DELETE A GCP PROJECT !!"
echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
echo ""
echo "   Project to be deleted: $GCP_PROJECT_ID"
echo ""
echo "This action cannot be undone. It will delete all services, data, and"
echo "resources associated with this project."
echo ""
read -p "Are you absolutely sure you want to proceed? (yes/no): " confirmation

if [ "$confirmation" != "yes" ]; then
    echo "❌ Deletion cancelled. No changes were made."
    exit 0
fi

# --- 3. Execute Deletion ---
echo ""
echo "▶️ Proceeding with deletion of project '$GCP_PROJECT_ID'..."
gcloud projects delete $GCP_PROJECT_ID

# --- 4. Final Status and Verification ---
echo ""
echo "✅ The 'delete' command has been issued for project '$GCP_PROJECT_ID'."
echo "GCP is now processing the deletion. This can take a few minutes."
echo ""
echo "To verify the deletion status:"
echo "1. Go to the Google Cloud Console: https://console.cloud.google.com/"
echo "2. Navigate to 'IAM & Admin' -> 'Manage Resources'."
echo "3. The project should be listed with a 'Pending Deletion' status or disappear"
echo "   from the list once the process is complete."
echo ""
echo "🔥 Self-destruct sequence complete. 🔥"
