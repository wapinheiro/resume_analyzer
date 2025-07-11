# Resume Analyzer - Cost Analysis & Budget Planning

## 🎯 **Executive Summary**

This document provides a comprehensive cost breakdown for the Resume Analyzer project, emphasizing **minimal MVP investment** to demonstrate feasibility before scaling. The MVP is designed to be **self-fundable** if necessary, with clear scaling costs for institutional planning.

---

## 💰 **MVP Development Phase: Cost Analysis**

**Total Cost: $0**

Thanks to our **"Cloud-Ready Local"** development strategy, the entire Minimum Viable Product (MVP) will be developed, tested, and demonstrated without incurring any cloud infrastructure or service costs.

-   **Infrastructure**: The backend (FastAPI) and vector database (ChromaDB) will run locally in Docker containers via Docker Compose. The frontend (React) will run with a local Node.js server.
-   **LLM/AI Services**: The free tiers for Google Gemini, Serper.dev, and other planned services are sufficient for all development and testing needs.
-   **Tooling**: All development tools (VS Code, Docker Desktop, Git) are free for this use case.

This zero-cost approach allows us to deliver a fully functional, production-ready prototype for departmental review, making the decision to fund the operational phase a low-risk investment in a proven asset.

---

## 🚀 **Post-Deployment: Operational Cost Projections**

Once the MVP is approved and deployed to the university's official GCP environment, we anticipate the following monthly operational costs. These costs are usage-based and will scale with student adoption.

### **Scenario 1: Initial Pilot (First 100-200 Student Users)**

| Service | Estimated Monthly Usage | Estimated Monthly Cost | Notes |
| :--- | :--- | :--- | :--- |
| **GCP Cloud Run** (Backend) | ~500,000 requests, 2 vCPU-hours/day | $5 - $15 | Scales to zero, very cost-effective. |
| **Firebase Hosting** (Frontend) | ~10 GB egress, 50k requests | $0 (Free Tier) | Free tier is generous. |
| **Vertex AI** (Gemini 1.5 Flash) | ~2,000 analyses (5 agents/resume) | $10 - $25 | The primary operational cost. |
| **Serper.dev** (Web Search) | ~2,000 searches | $0 (Free Tier) | Free tier covers 2,500 queries. |
| **Contingency (25%)** | | $4 - $10 | For unexpected traffic spikes. |
| **Total Estimated Monthly Cost** | | **$19 - $50** | **A very affordable starting point.** |

### **Scenario 2: Full Department Adoption (~1,000 Active Users)**

| Service | Estimated Monthly Usage | Estimated Monthly Cost |
| :--- | :--- | :--- |
| **GCP Cloud Run** | ~2.5M requests, 10 vCPU-hours/day | $25 - $50 |
| **Firebase Hosting** | ~50 GB egress | $1 - $5 |
| **Vertex AI** (Gemini 1.5 Flash) | ~10,000 analyses | $50 - $125 |
| **Serper.dev** | ~10,000 searches | $8 (Pro Plan) |
| **Contingency (25%)** | | $21 - $46 |
| **Total Estimated Monthly Cost**| | **$105 - $234** | |

### **Budget Control and Monitoring**

-   **GCP Budgets & Alerts**: We will set strict budgets in the GCP project to automatically alert administrators if costs are projected to exceed thresholds.
-   **Cloud Run Scaling Limits**: We can configure maximum instance limits on Cloud Run to prevent unexpected cost spikes from traffic surges.
-   **Usage Analytics**: The system will include a dashboard to monitor the number of analyses being run, allowing for proactive cost management.

---

## 💸 **Funding Strategy**

### **Phase 1: Self-Funded (MVP Development)**
- **Cost**: $0
- **Source**: Developer time and expertise.

### **Phase 2: Departmental Sponsorship (Operational Launch)**
- **Ask**: We request an initial budget of **$500 for the first academic year** to cover the operational costs of the pilot program.
- **Justification**: This modest investment launches a powerful career tool for all CS students, directly impacting placement success and enhancing the department's reputation for innovation. The "Cloud-Ready" approach guarantees that these funds are used for live service delivery, not speculative development.
