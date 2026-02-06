from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import ai_routes,claim_routes


app = FastAPI(
    title="Insurance Claim Processor",
    description="AI-powered claim processing API",
    version="1.0.0"
)

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(ai_routes.router)
app.include_router(claim_routes.router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to Insurance Claim AI Processor",
        "docs": "/docs",
        "health": "/health"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "Server is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)