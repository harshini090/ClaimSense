from fastapi import APIRouter, UploadFile, File, HTTPException
import time
from datetime import datetime
from app.services.pdf_service import pdf_service
from app.services.ai_service import ai_service
from app.store import claims_store

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
    
    start_time = time.time()
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
            
            processing_time = time.time() - start_time
            fraud_flag = False
            
            if claim_result["success"]:
                extracted = claim_result.get("extracted_data", {})
                fraud_flag = extracted.get("fraud_flag", False) if isinstance(extracted, dict) else False
                claimant_name = extracted.get("Claimant Name", extracted.get("claimant_name", "Unknown")) if isinstance(extracted, dict) else "Unknown"
                claim_amount = extracted.get("Claim Amount", extracted.get("claim_amount", "$0")) if isinstance(extracted, dict) else "$0"
                
                response["claim_data"] = {
                    "extracted_info": extracted,
                    "ai_metadata": {
                        "model": claim_result["model"],
                        "tokens_used": claim_result["tokens_used"],
                        "cost": claim_result["cost_estimate"]
                    }
                }
                
                # Check if it was actually a claim before storing
                if isinstance(extracted, dict) and extracted.get("is_claim") is not False:
                    claims_store.append({
                        "id": f"CLM-{datetime.now().strftime('%Y%m%d')}-{len(claims_store)+1:03d}",
                        "timestamp": datetime.now().isoformat(),
                        "filename": file.filename,
                        "claimant_name": claimant_name,
                        "claim_amount": claim_amount,
                        "status": "Review" if fraud_flag else "Approved",
                        "fraud_flag": fraud_flag,
                        "processing_time_s": round(processing_time, 2),
                        "model": claim_result["model"]
                    })
                    
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