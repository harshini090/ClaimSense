import os
from anthropic import Anthropic
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class AIService:
    def __init__(self):
        """Initialize the Anthropic client"""
        api_key = os.getenv("ANTHROPIC_API_KEY")
        
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment variables")
        
        self.client = Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-20250514"  # Latest Claude model
    async def extract_claim_data(self, claim_text: str) -> dict:
        """
        Extract structured claim data from text using Claude
        
        Args:
            claim_text: The claim document text
            
        Returns:
            dict with extracted claim information
        """
        try:
            # Prompt Claude to extract claim data
            prompt = f"""You are an insurance claim processing assistant. 
First, determine if the provided text is an insurance claim document.
- If it IS NOT an insurance claim (e.g., it's a resume, recipe, code, generic article, etc.), return a JSON with:
  {{
    "is_claim": false,
    "error_message": "You have uploaded a document which is not relevant. Try uploading a document having about insurance claim details."
  }}
- If it IS an insurance claim, extract the following fields and return a JSON with "is_claim": true and the fields:

Extract these fields if present:
- Claimant Name
- Policy Number
- Claim Date
- Incident Date
- Claim Amount
- Claim Type (auto, health, property, etc.)
- Description of Incident
- Contact Information

Additionally, analyze the extracted data for potential fraud and confidence:
- "confidence_score": integer between 0-100 indicating extraction quality
- "fraud_flag": boolean indicating if suspicious patterns exist (e.g., highly unusual amounts, vague descriptions)
- "fraud_reasoning": string explaining the fraud_flag securely (empty or "N/A" if low risk)

Claim Document:
{claim_text}

Ensure the response is a valid JSON object. Do not include markdown."""

            message = self.client.messages.create(
                model=self.model,
                max_tokens=2048,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            
            response_text = message.content[0].text
            import json
            try:
                # Try to clean markdown code blocks if present
                clean_json = response_text.replace("```json", "").replace("```", "").strip()
                extracted_data = json.loads(clean_json)
            except json.JSONDecodeError:
                # Fallback to returning raw text if parsing fails
                extracted_data = {"raw_text": response_text, "error": "Failed to parse JSON"}
            
            return {
                "success": True,
                "extracted_data": extracted_data,
                "model": self.model,
                "tokens_used": message.usage.input_tokens + message.usage.output_tokens,
                "cost_estimate": self._calculate_cost(message.usage)
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def _calculate_cost(self, usage) -> dict:
        """Calculate approximate cost of API call"""
        # Claude Sonnet 4 pricing (approximate)
        input_cost_per_million = 3.0
        output_cost_per_million = 15.0
        
        input_cost = (usage.input_tokens / 1_000_000) * input_cost_per_million
        output_cost = (usage.output_tokens / 1_000_000) * output_cost_per_million
        total_cost = input_cost + output_cost
        
        return {
            "input_tokens": usage.input_tokens,
            "output_tokens": usage.output_tokens,
            "total_tokens": usage.input_tokens + usage.output_tokens,
            "estimated_cost_usd": round(total_cost, 6)
        }
    async def analyze_text(self, text: str) -> dict:
        """
        Send text to Claude and get a response
        
        Args:
            text: The text to analyze
            
        Returns:
            dict with the AI response
        """
        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                messages=[
                    {
                        "role": "user",
                        "content": text
                    }
                ]
            )
            
            # Extract the response text
            response_text = message.content[0].text
            
            return {
                "success": True,
                "response": response_text,
                "model": self.model,
                "tokens_used": message.usage.input_tokens + message.usage.output_tokens
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
        

# Create a singleton instance
ai_service = AIService()