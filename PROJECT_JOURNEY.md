# Building ClaimSense: A Technical Journey

## 🚀 The Vision
When I set out to build **ClaimSense**, the objective was twofold: 
1. **Solve a deeply manual workflow:** Insurance adjusters spend countless hours manually extracting unstructured data from PDFs and form images. I wanted to automate this using state-of-the-art AI.
2. **Elevate the UX:** Enterprise software is notoriously clunky. I wanted to prove that complex, data-heavy B2B tools can—and should—look like modern consumer applications. 

## 🏗️ Architecture & Tech Stack
To achieve real-time responsiveness and strict typing across the stack, I chose:
- **Frontend**: Next.js 14, React 18, and Tailwind CSS.
- **Backend**: Python, FastAPI, and Uvicorn.
- **AI Engine**: Anthropic's Claude 3.5 Sonnet, utilized for its exceptional reasoning and JSON-formatting capabilities.

### The "Swiss" Design System
I implemented a strict "Swiss International Style" aesthetic. This meant absolutely zero rounded corners, a stark monochromatic palette, and a perfect 12-column grid. By relying heavily on Framer Motion for micro-interactions (like hovering over claim results), the static, brutalist interface feels incredibly fluid and alive without sacrificing professionalism.

## 🚧 Challenges Faced & Overcome

### 1. Taming LLM Outputs for Production
Initially, having Claude read a PDF and return data was easy. Having it *consistently* return a parsable JSON schema without conversational filler was difficult. I overcame this by engineering a strict system prompt and utilizing Pydantic models on the backend to validate and sanitize the AI's output before the frontend ever touched it.

### 2. The Great Deployment Pivot
The most significant hurdle in this project wasn't writing the code—it was deploying it. 
My initial goal was to set up an enterprise-grade CI/CD pipeline targeting **Azure Web Apps**.
- I successfully wrote the GitHub Actions workflow (`azure-deploy.yml`), but hit a wall with Azure Active Directory permissions and missing Service Principal secrets. 
- Pivoting to **Google Cloud Run** presented a similar roadblock: cloud billing accounts are notoriously difficult to activate instantly for new projects.

**The Solution:** I shifted to a lightweight, free-tier PaaS strategy using **Render** and **GitHub Pages**. 

### 3. The Package Manager Bug
During the Render deployment, the backend repeatedly failed to build. Analyzing the Render logs revealed that Render's native Python environment was running an outdated version of Poetry (`v1.7.0`), which violently crashed when it encountered the newer `package-mode = false` configuration in my `pyproject.toml`.

To solve this permanently, I realized that relying on a platform's invisible build scripts is an anti-pattern. 
**The Fix:** I completely stripped Poetry out of the production build process. I generated a pristine `requirements.txt` file and pivoted to a **Docker container deployment**. By pushing a robust `Dockerfile` to Render, I bypassed their buggy native Python builder entirely and guaranteed that my exact environment would run flawlessly anywhere.

## 💡 Key Takeaways
1. **Containerization is King:** The debugging hours spent fighting platform-specific build environments (Render, Azure) reminded me why Docker exists. Moving forward, I will always default to Dockerfile deployments.
2. **Design Builds Trust:** The brutalist, high-contrast UI I built for ClaimSense doesn't just look good; it makes the AI feel infinitely more capable and trustworthy to the end-user.
3. **Agility:** Being able to pivot from a complex Azure CI/CD pipeline down to a static Next.js export and a Dockerized backend on Render demonstrates the importance of decoupling your frontend and backend infrastructure.

ClaimSense is currently actively processing claims and accurately detecting fraud heuristics, proving that beautiful design and powerful AI are a potent combination for solving traditional enterprise bottlenecks.
