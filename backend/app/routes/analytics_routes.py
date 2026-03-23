from fastapi import APIRouter
from app.store import claims_store
from typing import Dict, Any

router = APIRouter(prefix="/api/analytics", tags=["Analytics"])

@router.get("")
async def get_analytics() -> Dict[str, Any]:
    total_claims = len(claims_store)
    
    if total_claims == 0:
        return {
            "active_claims": 0,
            "processed_today": 0,
            "pending_review": 0,
            "fraud_rate": 0,
            "avg_resolution_time_s": 0,
            "recent_claims": []
        }
    
    # Calculate metrics
    fraud_claims = sum(1 for c in claims_store if c.get("fraud_flag") is True)
    fraud_rate = (fraud_claims / total_claims) * 100
    
    avg_resolution_time = sum(c.get("processing_time_s", 1.2) for c in claims_store) / total_claims
    
    # Sort by recent first
    recent_claims = sorted(claims_store, key=lambda x: x.get("timestamp", ""), reverse=True)[:10]
    
    return {
        "active_claims": total_claims,
        "processed_today": total_claims,  # simplified for demo
        "pending_review": fraud_claims,
        "fraud_rate": round(fraud_rate, 1),
        "avg_resolution_time_s": round(avg_resolution_time, 2),
        "recent_claims": recent_claims
    }
