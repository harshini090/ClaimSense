from pypdf import PdfReader
from typing import Optional
import io

class PDFService:
    """Service for extracting text from PDF documents"""
    
    async def extract_text_from_pdf(self, pdf_file: bytes) -> dict:
        """
        Extract text from a PDF file
        
        Args:
            pdf_file: PDF file as bytes
            
        Returns:
            dict with extracted text and metadata
        """
        try:
            # Create a file-like object from bytes
            pdf_stream = io.BytesIO(pdf_file)
            
            # Read the PDF
            reader = PdfReader(pdf_stream)
            
            # Extract text from all pages
            text_content = []
            for page_num, page in enumerate(reader.pages, start=1):
                page_text = page.extract_text()
                if page_text.strip():  # Only add non-empty pages
                    text_content.append({
                        "page": page_num,
                        "text": page_text
                    })
            
            # Combine all text
            full_text = "\n\n".join([p["text"] for p in text_content])
            
            return {
                "success": True,
                "text": full_text,
                "page_count": len(reader.pages),
                "pages": text_content,
                "metadata": {
                    "total_pages": len(reader.pages),
                    "pages_with_text": len(text_content)
                }
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Failed to extract PDF text: {str(e)}"
            }
    
    def clean_text(self, text: str) -> str:
        """
        Clean extracted text (remove extra whitespace, etc.)
        
        Args:
            text: Raw extracted text
            
        Returns:
            Cleaned text
        """
        # Remove multiple spaces
        text = " ".join(text.split())
        
        # Remove multiple newlines
        lines = [line.strip() for line in text.split("\n") if line.strip()]
        text = "\n".join(lines)
        
        return text

# Create singleton instance
pdf_service = PDFService()