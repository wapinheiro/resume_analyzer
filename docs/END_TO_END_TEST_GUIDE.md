# End-to-End Test Execution Guide

This document provides the steps and commands to run an end-to-end test for the Resume Analyzer project.

## Prerequisites
- Ensure all dependencies are installed for both backend and frontend.
- Python and Node.js should be installed on your system.
- A Python virtual environment (`venv`) exists in the `backend` folder.

## Steps


### 1. Activate Python Virtual Environment (Backend)
```
cd backend
source venv/bin/activate
```

#### How to Verify the Backend Server is Running

After running `python main.py`, there are two ways to confirm the backend server is running:

1. **Terminal Output:**
   - Look for a message like `Resume Analyzer API is running.` or a FastAPI/uvicorn startup message in your terminal.

2. **API Health Check:**
   - Open your browser and go to: `http://localhost:8000/`
   - You should see a JSON response:
     ```json
     {
       "status": "ok",
       "message": "Resume Analyzer API is running."
     }
     ```
   - Alternatively, you can run this command in another terminal:
     ```sh
     curl http://localhost:8000/
     ```
   - If you get the JSON response above, your backend server is running correctly.

### 2. Install Backend Dependencies
```
pip install -r requirements.txt
```

### 2. Start Backend Server
```
uvicorn main:app --reload
```
This will start the FastAPI backend server with hot-reload enabled. You should see FastAPI/uvicorn startup messages in the terminal, confirming the server is running.

### 3. Install Frontend Dependencies
```
cd ../frontend
npm install
```

### 4. Start Frontend Server
```
npm start
```

### 5. Run End-to-End Test
- Open your browser and navigate to the frontend URL (usually http://localhost:3000).
- Interact with the application as needed to verify end-to-end functionality.

## Notes
 - Make sure both servers (backend and frontend) are running before testing.
 - If you encounter issues, check the terminal output for errors.
 - To deactivate the Python virtual environment, run `deactivate` in the terminal.

// ...existing code...

---
_Last updated: July 25, 2025_
