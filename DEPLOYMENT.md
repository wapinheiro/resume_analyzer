# Deployment Guide

This document provides instructions for deploying the Resume Analyzer application.

## Architecture

- **Frontend**: React app deployed on Vercel
- **Backend**: FastAPI app deployed on Google Cloud Run
- **Database**: Google Cloud Vertex AI (Gemini 2.5 Flash)

## Backend Deployment (Google Cloud Run)

The backend is already deployed and running at:
`https://resume-analyzer-api-895708803691.us-central1.run.app`

### Manual Redeployment

To redeploy the backend after making changes:

1. Build and push the Docker image:
```bash
cd backend
docker build --platform linux/amd64 -t gcr.io/resumeanalyzer-465907/resume-analyzer-api .
docker push gcr.io/resumeanalyzer-465907/resume-analyzer-api
```

2. Deploy to Cloud Run:
```bash
gcloud run deploy resume-analyzer-api \
  --image gcr.io/resumeanalyzer-465907/resume-analyzer-api \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --port 8080 \
  --set-env-vars "GOOGLE_CLOUD_PROJECT=resumeanalyzer-465907"
```

## Frontend Deployment (Vercel)

### Prerequisites

1. Install Vercel CLI:
```bash
npm install -g vercel
```

2. Login to Vercel:
```bash
vercel login
```

### Deploy to Vercel

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Deploy:
```bash
vercel --prod
```

Or use the Vercel dashboard:
1. Connect your GitHub repository to Vercel
2. Set the following environment variables:
   - `REACT_APP_API_URL`: `https://resume-analyzer-api-895708803691.us-central1.run.app`

### Local Development

For local development, create a `.env` file in the `frontend` directory:
```bash
REACT_APP_API_URL=http://localhost:8000
```

## Environment Variables

### Backend (Google Cloud Run)
- `GOOGLE_CLOUD_PROJECT`: `resumeanalyzer-465907`

### Frontend (Vercel)
- `REACT_APP_API_URL`: `https://resume-analyzer-api-895708803691.us-central1.run.app`

## Testing Deployment

### Backend Health Check
```bash
curl https://resume-analyzer-api-895708803691.us-central1.run.app/health
```

### Frontend
Visit your Vercel deployment URL and test the resume analysis functionality.

## Troubleshooting

### CORS Issues
If you encounter CORS issues, verify that the backend's CORS configuration in `backend/main.py` includes your frontend domain.

### Environment Variables
Ensure all environment variables are set correctly in both Vercel and Google Cloud Run.

### Build Issues
For frontend build issues, check that all dependencies are installed:
```bash
cd frontend
npm install
npm run build
```

## Cost Considerations

- **Google Cloud Run**: Pay-per-use, scales to zero when not in use
- **Vercel**: Free tier available, scales automatically
- **Vertex AI**: Pay-per-API-call for Gemini model usage

## Security Notes

- Backend is configured with proper CORS settings
- Environment variables are used for sensitive configuration
- Google Cloud project uses IAM for access control
