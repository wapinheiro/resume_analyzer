# GitHub Actions Workflows

This directory contains automated workflows for Continuous Integration and Deployment.

## 📋 Workflows

### CI Pipeline (`ci.yml`)

**Triggers:**
- Push to `dev` or `main` branches
- Pull requests to `dev` or `main` branches

**Jobs:**

#### 1. Backend Tests
- Sets up Python 3.10
- Installs dependencies from `backend/requirements.txt`
- Runs flake8 linting for code quality
- Executes pytest with coverage reporting

#### 2. Frontend Tests
- Sets up Node.js 18
- Installs npm dependencies
- Runs React build verification
- Executes Jest tests with coverage

#### 3. Build Verification
- Runs after both backend and frontend tests pass
- Verifies production build works
- Confirms backend can start
- Reports overall success

## ✅ Status Badges

You can add these badges to your main README.md:

```markdown
![CI Pipeline](https://github.com/wapinheiro/resume_analyzer/workflows/CI%20Pipeline/badge.svg)
```

## 🔧 Local Testing

To run the same tests locally before pushing:

### Backend
```bash
cd backend
pip install -r requirements.txt
flake8 .
pytest --cov=. --cov-report=term-missing
```

### Frontend
```bash
cd frontend
npm ci
npm test -- --coverage --watchAll=false
npm run build
```

## 🚀 Adding More Workflows

To add additional workflows (e.g., deployment, security scanning):

1. Create a new `.yml` file in this directory
2. Define the trigger conditions
3. Add the necessary jobs and steps
4. Commit and push to activate

## 📚 Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow Syntax](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)
- [Available Actions](https://github.com/marketplace?type=actions)

