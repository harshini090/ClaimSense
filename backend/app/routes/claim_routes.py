from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.pdf_service import pdf_service
from app.services.ai_service import ai_service

router = APIRouter(prefix="/api/claims", tags=["Claims"])

@router.post("/process")
async def process_claim(
    file: UploadFile = File(..., description="PDF claim document"),
    extract_data: bool = True
):
    """
    Process an insurance claim PDF document
    
    Steps:
    1. Extract text from PDF
    2. Optionally use AI to extract structured claim data
    3. Return processed information
    """
    
    # Validate file type
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(
            status_code=400, 
            detail="Only PDF files are supported"
        )
    
    try:
        # Read the uploaded file
        pdf_content = await file.read()
        
        # Extract text from PDF
        pdf_result = await pdf_service.extract_text_from_pdf(pdf_content)
        
        if not pdf_result["success"]:
            raise HTTPException(
                status_code=500,
                detail=pdf_result.get("error", "PDF extraction failed")
            )
        
        # Clean the extracted text
        cleaned_text = pdf_service.clean_text(pdf_result["text"])
        
        response = {
            "success": True,
            "filename": file.filename,
            "pdf_metadata": pdf_result["metadata"],
            "extracted_text": cleaned_text[:1000] + "..." if len(cleaned_text) > 1000 else cleaned_text,
        }
        
        # If requested, extract structured claim data using AI
        if extract_data:
            claim_result = await ai_service.extract_claim_data(cleaned_text)
            
            if claim_result["success"]:
                response["claim_data"] = {
                    "extracted_info": claim_result["extracted_data"],
                    "ai_metadata": {
                        "model": claim_result["model"],
                        "tokens_used": claim_result["tokens_used"],
                        "cost": claim_result["cost_estimate"]
                    }
                }
            else:
                response["claim_data"] = {
                    "error": claim_result.get("error", "AI extraction failed")
                }
        
        return response
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process claim: {str(e)}"
        )

@router.post("/extract-text")
async def extract_text_only(file: UploadFile = File(...)):
    """
    Extract text from PDF without AI processing
    
    Useful for testing or when you only need the raw text
    """
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")
    
    try:
        pdf_content = await file.read()
        result = await pdf_service.extract_text_from_pdf(pdf_content)
        
        if not result["success"]:
            raise HTTPException(status_code=500, detail=result.get("error"))
        
        return {
            "success": True,
            "filename": file.filename,
            "text": result["text"],
            "metadata": result["metadata"]
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))