# 🏛️ ClaimSense AI
> **Intelligence built into the design.**  
> A next-generation insurance claim processing platform engineered for speed, accuracy, and absolute clarity.

<p align="center">
  <img src="assets/demo.webp?raw=true" alt="ClaimSense Live Interface Demo" width="100%">
</p>

## 🌟 The Vision
Insurance claim processing is traditionally bogged down by manual data entry, unstructured PDFs, and slow risk assessment. **ClaimSense** shifts this paradigm by leveraging advanced Large Language Models to analyze claim documents in real-time, instantly extracting vital data and flagging potential fraud—all wrapped in a stark, "Swiss International / Braun" inspired design system.

---

## ✨ Core Capabilities

- **🧠 Real-time AI Extraction**: Powered by **Claude 3.5 Sonnet**, ClaimSense instantly parses unstructured PDF and image uploads to extract claimant data, policy numbers, incident descriptions, and calculate claim totals.
- **🛡️ Intelligent Fraud Detection**: Evaluates incidents for potential fraud patterns, returning a comprehensive risk assessment (Low, Medium, or High Risk) with logically cited reasoning.
- **👁️ Objectively Beautiful UI**: Designed with the philosophy that "perfection is achieved when there is nothing left to take away." Pure white backgrounds, jet black typography, and strict 12-column grid alignment.
- **🔄 Developer-First Transparency**: Seamlessly switch between a clean visual summary for adjusters and raw JSON data payloads for developers.

---

## 🛠 Technology Stack

### Frontend Architecture
![Next JS](https://img.shields.io/badge/Next-black?style=for-the-badge&logo=next.js&logoColor=white)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Framer](https://img.shields.io/badge/Framer-black?style=for-the-badge&logo=framer&logoColor=blue)
- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS (Custom Monochromatic Aesthetic)
- **Animations**: Framer Motion

### Backend Engine
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Claude](https://img.shields.io/badge/Claude%203.5-Anthropic-D97757?style=for-the-badge&logo=anthropic)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
- **Framework**: FastAPI (High-performance asynchronous API)
- **Language**: Python 3.9
- **AI Brain**: Anthropic API (`claude-3-5-sonnet-20241022`)
- **Containerization**: Docker Multi-stage Builds

---

## 🚀 Local Development Setup

ClaimSense is fully containerized for a scalable, environment-agnostic deployment. 

### Prerequisites
- Docker & Docker Compose
- An Anthropic API Key (`claude-3-5-sonnet`)

### 1. Backend (FastAPI) Setup
```bash
git clone https://github.com/harshini090/ClaimSense.git
cd ClaimSense/backend

# Configure Environment Variables
echo "ANTHROPIC_API_KEY=your_api_key_here" > .env
echo "ENVIRONMENT=development" >> .env

# Build and run with Docker
docker build -t claim-backend:latest .
docker run -p 8000:8000 --env-file .env claim-backend:latest
```
> The API will be available at `http://127.0.0.1:8000` (Interactive Docs at `/docs`)

### 2. Frontend (Next.js) Setup
```bash
cd ../frontend

# Configure API target
echo "NEXT_PUBLIC_API_URL=http://127.0.0.1:8000" > .env.local

# Run Next.js locally
npm install
npm run dev
```
> Access the UI at `http://localhost:3000`

---

## ☁️ Deployment Strategy

The application is designed to be completely decoupled.
- The **Frontend** can be statically exported and hosted on Vercel, Netlify, or GitHub Pages.
- The **Backend** is completely containerized (`backend/Dockerfile`) utilizing a stable `requirements.txt` environment, ensuring deployment to any PaaS (Render, Google Cloud Run, Azure Container Apps) is trivial and resistant to package manager conflicts.

## 📄 License
MIT License.
