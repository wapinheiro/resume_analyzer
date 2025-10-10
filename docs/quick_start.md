# Running Resume Analyzer: Quick Start Guide

## Backend (FastAPI)

1. Open a terminal and navigate to the backend directory:
   ```sh
   cd /Users/wagnerp2/Documents/byu/resume_analyzer/backend
   ```
2. Activate the Python virtual environment:
   ```sh
   source venv/bin/activate
   ```
3. (Optional) Install dependencies if not already done:
   ```sh
   pip install -r requirements.txt
   ```
4. Start the FastAPI server:
   ```sh
   uvicorn main:app --reload
   ```
   - The server will run at http://127.0.0.1:8000

## Frontend (React)

1. Open a new terminal and navigate to the frontend directory:
   ```sh
   cd /Users/wagnerp2/Documents/byu/resume_analyzer/frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the frontend development server:
   ```sh
   npm start
   ```
   - The frontend will run at http://localhost:3000

## Troubleshooting
- If you see `Could not import module "main"`, make sure you are in the `backend` directory and that `main.py` contains a FastAPI app named `app`.
- If you have issues with dependencies, re-run `pip install -r requirements.txt` in the backend or `npm install` in the frontend.

## Usage
- Upload your resume PDF via the frontend interface.
- The backend will analyze and score your resume using AI agents.
- Results and feedback will be displayed in the frontend.

---
For more details, see the main README.md in the project root.
