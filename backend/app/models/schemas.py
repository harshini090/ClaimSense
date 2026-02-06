from pydantic import BaseModel, Field
from typing import Optional

class TextAnalysisRequest(BaseModel):
    """Request model for text analysis"""
    text: str = Field(..., description="Text to analyze", min_length=1)
    
    class Config:
        json_schema_extra = {
            "example": {
                "text": "This is a sample insurance claim for a car accident."
            }
        }

class TextAnalysisResponse(BaseModel):
    """Response model for text analysis"""
    success: bool
    response: Optional[str] = None
    model: Optional[str] = None
    tokens_used: Optional[int] = None
    error: Optional[str] = None
from fastapi import UploadFile

class ClaimProcessRequest(BaseModel):
    """Request model for claim processing"""
    extract_structured_data: bool = Field(
        default=True, 
        description="Whether to extract structured data using AI"
    )

class ClaimProcessResponse(BaseModel):
    """Response model for claim processing"""
    success: bool
    filename: str
    pdf_metadata: Optional[dict] = None
    extracted_text: Optional[str] = None
    claim_data: Optional[dict] = None
    error: Optional[str] = None
    