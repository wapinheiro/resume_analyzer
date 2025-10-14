# Deployment Implementation Plan
## Resume Analyzer - Separate Deployment Strategy

**Target Architecture:** Frontend (Vercel) + Backend (Google Cloud Run)  
**Created:** $(date)  
**Status:** Ready for Implementation  

---

## 🎯 Overview

This document outlines the step-by-step implementation plan for deploying the Resume Analyzer application using a separate deployment strategy:

- **Frontend**: React app deployed to Vercel (CDN + automatic deployments)
- **Backend**: FastAPI server deployed to Google Cloud Run (containerized + auto-scaling)

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    USERS                                │
│              (Resume Upload & Analysis)                 │
└─────────────┬───────────────────────────────────────────┘
              │
              │ HTTPS
              ▼
┌─────────────────────────────────────────────────────────┐
│  FRONTEND (Vercel CDN)                                 │
│  ├─ React App (Static Files)                           │
│  ├─ Global CDN Distribution                            │
│  ├─ Automatic Deployments from GitHub                  │
│  └─ Preview Deployments for PRs                        │
└─────────────┬───────────────────────────────────────────┘
              │
              │ API Calls (CORS enabled)
              ▼
┌─────────────────────────────────────────────────────────┐
│  BACKEND (Google Cloud Run)                            │
│  ├─ FastAPI Server (Containerized)                     │
│  ├─ Auto-scaling (0 to N instances)                    │
│  ├─ Vertex AI Integration                              │
│  └─ HTTPS Termination                                  │
└─────────────────────────────────────────────────────────┘
```

---

## 📋 Implementation Phases

### **Phase 1: Backend Deployment Setup**
*Estimated Time: 2-3 hours*

#### 1.1 Create Docker Configuration
- [ ] Create `backend/Dockerfile`
- [ ] Create `backend/.dockerignore`
- [ ] Test Docker build locally
- [ ] Verify FastAPI app starts correctly in container

#### 1.2 Google Cloud Setup
- [ ] Install Google Cloud CLI
- [ ] Authenticate with Google Cloud
- [ ] Create or select Google Cloud project
- [ ] Enable Cloud Run API
- [ ] Enable Vertex AI API

#### 1.3 Deploy to Cloud Run
- [ ] Build and push Docker image to Google Container Registry
- [ ] Deploy container to Cloud Run
- [ ] Configure environment variables
- [ ] Test API endpoints
- [ ] Set up custom domain (optional)

#### 1.4 CORS Configuration
- [ ] Update FastAPI CORS middleware
- [ ] Configure allowed origins for Vercel domains
- [ ] Test CORS from browser

---

### **Phase 2: Frontend Deployment Setup**
*Estimated Time: 1-2 hours*

#### 2.1 Vercel Account Setup
- [ ] Create Vercel account (if needed)
- [ ] Connect GitHub repository to Vercel
- [ ] Configure build settings for React app

#### 2.2 Frontend Configuration
- [ ] Create `frontend/vercel.json` configuration
- [ ] Update environment variables for API URL
- [ ] Configure build command and output directory

#### 2.3 Deploy to Vercel
- [ ] Deploy frontend to Vercel
- [ ] Configure custom domain (optional)
- [ ] Test frontend-backend integration
- [ ] Verify file upload and analysis flow

---

### **Phase 3: CI/CD Integration**
*Estimated Time: 1-2 hours*

#### 3.1 GitHub Actions for Deployment
- [ ] Create `.github/workflows/deploy-backend.yml`
- [ ] Create `.github/workflows/deploy-frontend.yml`
- [ ] Configure secrets in GitHub repository

#### 3.2 Environment Management
- [ ] Set up staging environment
- [ ] Configure environment-specific variables
- [ ] Test deployment pipeline

#### 3.3 Monitoring Setup
- [ ] Set up Google Cloud monitoring
- [ ] Configure error tracking (optional)
- [ ] Set up uptime monitoring (optional)

---

### **Phase 4: Testing & Optimization**
*Estimated Time: 1-2 hours*

#### 4.1 End-to-End Testing
- [ ] Test complete user workflow
- [ ] Performance testing
- [ ] Load testing (optional)
- [ ] Security testing

#### 4.2 Documentation
- [ ] Update README with deployment info
- [ ] Document environment variables
- [ ] Create troubleshooting guide

---

## 📁 File Structure

After implementation, the project will have:

```
resume_analyzer_1.2/
├── backend/
│   ├── Dockerfile                    # NEW: Container configuration
│   ├── .dockerignore                 # NEW: Docker ignore rules
│   ├── requirements.txt              # UPDATED: Production dependencies
│   ├── main.py                       # EXISTING: FastAPI app
│   └── ...
├── frontend/
│   ├── vercel.json                   # NEW: Vercel configuration
│   ├── package.json                  # EXISTING: React dependencies
│   └── ...
├── .github/
│   └── workflows/
│       ├── ci.yml                    # EXISTING: CI pipeline
│       ├── deploy-backend.yml        # NEW: Backend deployment
│       └── deploy-frontend.yml       # NEW: Frontend deployment
└── docs/
    ├── DEPLOYMENT_IMPLEMENTATION_PLAN.md  # THIS FILE
    ├── CI_CD_SETUP.md               # EXISTING: CI documentation
    └── ...
```

---

## 🔧 Detailed Implementation Steps

### **Step 1: Backend Docker Setup**

#### Create `backend/Dockerfile`:
```dockerfile
# Use Python 3.10 slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash app \
    && chown -R app:app /app
USER app

# Expose port
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
```

#### Create `backend/.dockerignore`:
```
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv/
pip-log.txt
pip-delete-this-directory.txt
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.log
.git/
.mypy_cache/
.pytest_cache/
.hypothesis/
.DS_Store
```

### **Step 2: Google Cloud Setup**

#### Commands to run:
```bash
# Install Google Cloud CLI (if not installed)
# Follow: https://cloud.google.com/sdk/docs/install

# Authenticate
gcloud auth login

# Set project
gcloud config set project YOUR_PROJECT_ID

# Enable APIs
gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com
gcloud services enable aiplatform.googleapis.com

# Configure Docker for GCR
gcloud auth configure-docker
```

### **Step 3: Frontend Vercel Setup**

#### Create `frontend/vercel.json`:
```json
{
  "buildCommand": "npm run build",
  "outputDirectory": "build",
  "framework": "create-react-app",
  "installCommand": "npm ci",
  "env": {
    "REACT_APP_API_URL": "@react_app_api_url"
  },
  "rewrites": [
    {
      "source": "/(.*)",
      "destination": "/index.html"
    }
  ]
}
```

### **Step 4: GitHub Actions Deployment**

#### Create `.github/workflows/deploy-backend.yml`:
```yaml
name: Deploy Backend to Cloud Run

on:
  push:
    branches: [main]
    paths: ['backend/**']

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v4
    
    - name: Set up Google Cloud CLI
      uses: google-github-actions/setup-gcloud@v2
      with:
        project_id: ${{ secrets.GCP_PROJECT_ID }}
        service_account_key: ${{ secrets.GCP_SA_KEY }}
        export_default_credentials: true
    
    - name: Configure Docker
      run: gcloud auth configure-docker
    
    - name: Build and push Docker image
      run: |
        cd backend
        docker build -t gcr.io/${{ secrets.GCP_PROJECT_ID }}/resume-analyzer-api .
        docker push gcr.io/${{ secrets.GCP_PROJECT_ID }}/resume-analyzer-api
    
    - name: Deploy to Cloud Run
      run: |
        gcloud run deploy resume-analyzer-api \
          --image gcr.io/${{ secrets.GCP_PROJECT_ID }}/resume-analyzer-api \
          --platform managed \
          --region us-central1 \
          --allow-unauthenticated \
          --set-env-vars "VERTEX_AI_PROJECT_ID=${{ secrets.VERTEX_AI_PROJECT_ID }}"
```

#### Create `.github/workflows/deploy-frontend.yml`:
```yaml
name: Deploy Frontend to Vercel

on:
  push:
    branches: [main]
    paths: ['frontend/**']

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v4
    
    - name: Deploy to Vercel
      uses: amondnet/vercel-action@v25
      with:
        vercel-token: ${{ secrets.VERCEL_TOKEN }}
        vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
        vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
        working-directory: ./frontend
```

---

## 🔐 Required Secrets

Configure these in GitHub repository settings:

### **Google Cloud Secrets:**
- `GCP_PROJECT_ID`: Your Google Cloud project ID
- `GCP_SA_KEY`: Service account JSON key (for automated deployments)
- `VERTEX_AI_PROJECT_ID`: Project ID for Vertex AI

### **Vercel Secrets:**
- `VERCEL_TOKEN`: Personal access token from Vercel
- `VERCEL_ORG_ID`: Organization ID from Vercel
- `VERCEL_PROJECT_ID`: Project ID from Vercel

### **Application Secrets:**
- `REACT_APP_API_URL`: Backend API URL (set in Vercel dashboard)

---

## 💰 Cost Estimates

### **Free Tier Usage (< 10K requests/month):**
- **Vercel**: $0 (100GB bandwidth, unlimited static hosting)
- **Google Cloud Run**: $0 (2 million requests, 400,000 vCPU-seconds)
- **Total**: **$0/month**

### **Light Usage (100K requests/month):**
- **Vercel**: $0
- **Google Cloud Run**: $5-10
- **Total**: **$5-10/month**

### **Heavy Usage (1M requests/month):**
- **Vercel**: $0-20 (if bandwidth exceeded)
- **Google Cloud Run**: $40-60
- **Total**: **$40-80/month**

---

## 🚨 Potential Issues & Solutions

### **Issue 1: CORS Errors**
**Problem**: Frontend can't call backend API  
**Solution**: Configure CORS in FastAPI with Vercel domains

### **Issue 2: Environment Variables**
**Problem**: Secrets not available in production  
**Solution**: Set up GitHub Secrets and Vercel environment variables

### **Issue 3: File Upload Size Limits**
**Problem**: Large resume files fail to upload  
**Solution**: Configure Cloud Run request size limits

### **Issue 4: Cold Start Latency**
**Problem**: First request to Cloud Run is slow  
**Solution**: Implement health checks or keep-warm endpoint

---

## ✅ Success Criteria

The deployment is successful when:

1. **Backend API is accessible** at `https://api.yourdomain.com`
2. **Frontend is accessible** at `https://yourdomain.com`
3. **File upload works** from frontend to backend
4. **AI analysis completes** successfully end-to-end
5. **CORS is properly configured** for cross-origin requests
6. **Automatic deployments work** on push to main branch
7. **Health checks pass** for both services
8. **Costs are within budget** (ideally $0 for initial usage)

---

## 📅 Timeline

| Phase | Duration | Dependencies |
|-------|----------|--------------|
| Phase 1: Backend | 2-3 hours | Google Cloud account |
| Phase 2: Frontend | 1-2 hours | Vercel account |
| Phase 3: CI/CD | 1-2 hours | GitHub repository access |
| Phase 4: Testing | 1-2 hours | Phases 1-3 complete |
| **Total** | **5-9 hours** | |

---

## 🎯 Next Steps

1. **Review and approve** this implementation plan
2. **Commit and push** this document to repository
3. **Merge to dev branch** for team visibility
4. **Begin Phase 1** implementation when ready

---

## 📚 Resources

- [Google Cloud Run Documentation](https://cloud.google.com/run/docs)
- [Vercel Documentation](https://vercel.com/docs)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [FastAPI Deployment Guide](https://fastapi.tiangolo.com/deployment/)
- [React Deployment Guide](https://create-react-app.dev/docs/deployment/)

---

*This document will be updated as implementation progresses and lessons are learned.*
