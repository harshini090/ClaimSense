from fpdf import FPDF

# Create Sample Claim PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Insurance Claim Form", ln=1, align="C")
pdf.ln(10)
pdf.multi_cell(0, 10, txt="Claimant Name: Sarah Jenkins\nPolicy Number: POL-99231-USA\nClaim Date: October 24, 2024\nIncident Date: October 22, 2024\nClaim Amount: $1,250.00\nClaim Type: Auto Insurance\nContact Information: sarah.j@example.com / 555-0198\n\nDescription of Incident:\nI was driving down Main St. when a deer jumped out of the bushes. I swerved to avoid it and hit a mailbox, damaging the front right bumper and headlight.")
pdf.output("../sample_claim.pdf")

# Create Suspicious Claim PDF
pdf2 = FPDF()
pdf2.add_page()
pdf2.set_font("Arial", size=12)
pdf2.cell(200, 10, txt="Insurance Claim Form", ln=1, align="C")
pdf2.ln(10)
pdf2.multi_cell(0, 10, txt="Claimant Name: John Doe\nPolicy Number: POL-00000-XYZ\nClaim Date: November 01, 2024\nIncident Date: November 01, 2024\nClaim Amount: $950,000.00\nClaim Type: Property\nContact Information: john.doe@unknown.com\n\nDescription of Incident:\nI lost my very expensive watch while I was sleeping. I need the money transferred immediately.")
pdf2.output("../suspicious_claim.pdf")

# Create Irrelevant Doc PDF
pdf3 = FPDF()
pdf3.add_page()
pdf3.set_font("Arial", size=12)
pdf3.cell(200, 10, txt="My Best Chocolate Chip Cookie Recipe", ln=1, align="C")
pdf3.ln(10)
pdf3.multi_cell(0, 10, txt="Ingredients:\n- 2 cups flour\n- 1 cup sugar\n- 1 cup butter\n- 2 cups chocolate chips\n\nInstructions:\nMix everything together and bake at 350 for 12 minutes. Enjoy!")
pdf3.output("../irrelevant_doc.pdf")
