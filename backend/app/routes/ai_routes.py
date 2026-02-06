from fastapi import APIRouter, HTTPException
from app.models.schemas import TextAnalysisRequest, TextAnalysisResponse
from app.services.ai_service import ai_service

router = APIRouter(prefix="/api/ai", tags=["AI"])

@router.post("/analyze", response_model=TextAnalysisResponse)
async def analyze_text(request: TextAnalysisRequest):
    """
    Analyze text using Claude AI
    
    This endpoint demonstrates basic AI integration.
    Send any text and get Claude's analysis back.
    """
    result = await ai_service.analyze_text(request.text)
    
    if not result["success"]:
        raise HTTPException(status_code=500, detail=result.get("error", "AI analysis failed"))
    
    return result

@router.get("/test")
async def test_ai_connection():
    """
    Test if AI service is working
    
    Simple endpoint to verify your API key and connection work.
    """
    test_result = await ai_service.analyze_text("Hello! Please respond with 'Connection successful!'")
    
    if test_result["success"]:
        return {
            "status": "connected",
            "message": "AI service is working!",
            "model": test_result["model"]
        }
    else:
        raise HTTPException(status_code=500, detail="AI connection failed")