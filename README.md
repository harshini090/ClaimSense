# ClaimSense AI

> **Intelligence built into the design.**
> A next-generation insurance claim processing platform engineered for speed, accuracy, and absolute clarity.

<p align="center">
  <img src="assets/demo.webp" alt="ClaimSense Swiss Design Demo" width="100%">
</p>

## 🌟 Overview
**ClaimSense** leverages advanced Large Language Models (Claude 3.5 Sonnet) to analyze claim documents in real-time. It provides immediate risk assessment, intelligent data extraction, and fraud heuristic capabilities—all wrapped in a stark, "Swiss International / Braun" inspired design system.

## ✨ Key Features
- **Objectively Beautiful UI**: Pure white backgrounds, jet black typography, and strict 12-column grid alignment. Designed with the philosophy that "perfection is achieved when there is nothing left to take away."
- **AI-Powered Analysis**: Automatically extracts claimant data, policy numbers, incident descriptions, and calculates totals from unstructured PDF/Image uploads.
- **Intelligent Risk Assessment**: Evaluates potential fraud patterns and flags claims as Low, Medium, or High Risk with cited reasoning.
- **Dual Verification Modes**: Seamlessly switch between a clean visual summary for adjusters and raw JSON data for developers.

## 🛠 Technology Stack
- **Frontend Core**: Next.js 14, React 18, TypeScript
- **Styling UI/UX**: Tailwind CSS (Custom "Swiss" aesthetic), Framer Motion, Lucide Icons
- **Backend API**: Python 3.9, FastAPI, Uvicorn (managed by Poetry)
- **AI Engine**: Anthropic Claude 3.5 Sonnet Integration
- **Infrastructure**: Azure App Services, Docker, GitHub Actions (CI/CD)

---

## 🚀 Getting Started

### Prerequisites
- Node.js (v18+)
- Python (v3.9+)
- Poetry (for Python dependency management)
- Docker (for containerized environments)

### 1. Local Development Setup

#### Backend Infrastructure
The backend is a high-performance FastAPI service.
```bash
git clone https://github.com/harshini090/insurance-claim-ai.git
cd insurance-claim-ai/backend

# Install dependencies using Poetry
poetry install

# Configure Environment Variables
# Create a .env file in the backend directory:
echo "ANTHROPIC_API_KEY=your_api_key_here" > .env
echo "ENVIRONMENT=development" >> .env

# Launch the Uvicorn Dev Server
poetry run uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```
> The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000) (Swagger UI at `/docs`)

#### Frontend Infrastructure
The user interface is powered by Next.js.
```bash
cd ../frontend

# Install dependencies
npm install

# Optional: Add environment variables if your backend URL differs
# echo "NEXT_PUBLIC_API_URL=http://127.0.0.1:8000" > .env.local

# Launch the Next.js Dev Server
npm run dev
```
> Access the UI at [http://localhost:3000](http://localhost:3000) (or whichever port Next.js assigns).

---

## 🐳 Docker Deployment

ClaimSense is fully containerized for scalable, environment-agnostic deployment.

**Build the Backend Container:**
```bash
cd backend
docker build -t claim-backend:latest .
docker run -p 8000:8000 --env-file .env claim-backend:latest
```

**Build the Frontend Container:**
```bash
cd frontend
docker build -f Dockerfile.frontend -t claim-frontend:latest .
docker run -p 3000:3000 claim-frontend:latest
```

---

## ☁️ Azure Cloud Deployment (CI/CD)

This project features enterprise-grade CI/CD pipelines configured for **Azure Web Apps** via GitHub Actions.

1. **Azure Container Registry (ACR):** The pipeline builds Docker images for both frontend and backend and pushes them to your configured Azure Container Registry.
2. **Azure Web Apps deployed via Containers:** 
   - Backend API (`claim-sense-backend`)
   - Frontend UI (`claim-sense-frontend`)
3. **Automated Trigger:** Any push to the `main` branch automatically triggers the `azure-deploy.yml` workflow.

### Required GitHub Secrets for Azure:
Ensure the following secrets are configured in your repository settings:
- `AZURE_CREDENTIALS`
- `REGISTRY_LOGIN_SERVER`
- `REGISTRY_USERNAME`
- `REGISTRY_PASSWORD`
- `AZURE_BACKEND_PUBLISH_PROFILE`
- `AZURE_FRONTEND_PUBLISH_PROFILE`

---

## 📐 Design Philosophy
The UI follows the **Swiss International Style** (International Typographic Style), heavily relying on:
- **Monochromatic Palette**: Absolute contrast (`#FFFFFF` & `#000000`) with structural greys.
- **Typography-First Approach**: **Inter** (Grotesk Sans-Serif).
- **Subtlety**: Hover states and micro-animations provide tactile feedback without visual clutter.

## 📄 License
MIT License.
