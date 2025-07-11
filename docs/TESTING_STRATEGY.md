# Testing Strategy: The "Burner Project" Deployment

This document outlines the strategy for conducting a full, end-to-end test of the project's deployment scripts in a live cloud environment. The goal is to validate our single-command deployment process with zero long-term cost and no risk to personal or institutional cloud accounts.

## The "Burner Project" Philosophy

Instead of deploying to a persistent personal account, we create a temporary, disposable ("burner") Google Cloud Platform (GCP) project for the sole purpose of the test. Once the deployment is verified, the entire project is deleted, ensuring a complete and clean teardown.

This approach provides maximum confidence in our deployment automation while adhering to our principles of zero-cost development and avoiding complex environment migrations.

## The Testing Workflow

### Step 1: Create the Burner Project

1.  Navigate to the [Google Cloud Console](https://console.cloud.google.com/).
2.  Create a new GCP project. Name it something descriptive, like `resume-analyzer-test-deploy`.
3.  **Associate a billing account.** The test should be brief, and costs will be negligible or fall within the GCP Free Tier.
4.  **Enable the necessary APIs** for the new project. A prompt may guide you, but ensure the following are enabled:
    *   Cloud Run API
    *   Artifact Registry API (or Container Registry API)
    *   Cloud Build API
    *   Firebase Management API

### Step 2: Configure and Deploy

1.  Open `scripts/deployment.config.sh`.
2.  Fill in the `GCP_PROJECT_ID` and `FIREBASE_PROJECT_ID` variables with the unique ID of your newly created burner project.
3.  Authenticate your local command-line tools with your personal account:
    ```bash
    gcloud auth login
    firebase login
    ```
4.  Run the master deployment script from the `scripts` directory:
    ```bash
    ./deploy_all.sh
    ```

### Step 3: Verify the Deployment

The script will output the URLs for the live backend service and frontend application. Visit these URLs to confirm that the deployment was successful and the application is running as expected.

## The "Self-Destruct Button": `destroy_all.sh`

To ensure a clean and complete teardown, we have a "self-destruct" script that deletes the entire GCP project.

### How it Works

1.  **Configuration**: The script reads the `GCP_PROJECT_ID` from the `deployment.config.sh` file to target the correct burner project.
2.  **Confirmation**: To prevent accidental deletion, the script will prompt you to confirm that you want to permanently delete the specified project.
3.  **Execution**: Upon confirmation, the script executes the `gcloud projects delete` command. This is an asynchronous operation; GCP will begin the process of shutting down and deleting all resources within that project.
4.  **Verification**: The script will notify you that the deletion process has started. You can monitor the final deletion status in the "Manage Resources" section of the Google Cloud Console.

This testing strategy allows us to repeatedly and safely validate our deployment process, ensuring we are always ready for a production launch.
