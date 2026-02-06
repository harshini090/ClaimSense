
import sys

def create_resume_pdf(filename):
    pdf_content = (
        b"%PDF-1.4\n"
        b"1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj\n"
        b"2 0 obj<</Type/Pages/Kids[3 0 R]/Count 1>>endobj\n"
        b"3 0 obj<</Type/Page/MediaBox[0 0 595 842]/Parent 2 0 R/Resources<<>>/Contents 4 0 R>>endobj\n"
        b"4 0 obj<</Length 53>>stream\n"
        b"BT /F1 24 Tf 50 750 Td (Resume: John Doe Application) Tj ET\n"
        b"endstream\n"
        b"endobj\n"
        b"xref\n"
        b"0 5\n"
        b"0000000000 65535 f \n"
        b"0000000009 00000 n \n"
        b"0000000052 00000 n \n"
        b"0000000101 00000 n \n"
        b"0000000189 00000 n \n"
        b"trailer<</Size 5/Root 1 0 R>>\n"
        b"startxref\n"
        b"292\n"
        b"%%EOF\n"
    )
    
    with open(filename, 'wb') as f:
        f.write(pdf_content)
    print(f"Created {filename}")

if __name__ == "__main__":
    create_resume_pdf("irrelevant_doc.pdf")
