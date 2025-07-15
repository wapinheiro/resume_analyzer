# Resume Analyzer Backend

This directory contains the Python backend for the Resume Analyzer application.

## Setup Instructions

Follow these steps to set up and run the backend service.

### 1. Prerequisites

- Python 3.9+
- Google Cloud SDK (`gcloud`) installed and configured.
- A Google Cloud project with billing enabled.
- The Vertex AI API enabled in your Google Cloud project.

### 2. Environment Setup

1.  **Create and activate a Python virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### 3. Google Cloud Authentication

1.  **Log in with Application Default Credentials:**

    This command will open a browser window for you to authenticate with your Google account.

    ```bash
    gcloud auth application-default login
    ```

2.  **Set up the environment file:**

    Create a file named `.env` in this `backend` directory with the following content, replacing `<your-project-id>` with your actual Google Cloud project ID:

    ```
    GOOGLE_CLOUD_PROJECT=<your-project-id>
    ```

### 4. Running the Connection Test

To verify that your setup is correct and you can connect to the Vertex AI Gemini model, run the following command from the root `resume_analyzer` directory:

```bash
python3 backend/main.py
```

You should see a success message indicating that the connection was established.

### Notes

- **Model Availability:** The `main.py` script is currently configured to use the `gemini-2.5-flash` model. Google Cloud regularly updates its available models. If you encounter an error stating the model is not found, you may need to update the model name in `backend/main.py` to a currently available version.
- **Billing:** Ensure that billing is enabled for your Google Cloud project. The Vertex AI services used in this application are not free.
- **Permissions:** Your Google Cloud user account needs the "Vertex AI User" role (or a role with similar permissions) to access the Vertex AI services.
