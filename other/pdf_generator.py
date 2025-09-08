from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfgen import canvas

def generate_certificate(name, output_file="certificate.pdf"):
    c = canvas.Canvas(output_file, pagesize=landscape(A4))
    c.setFont("Helvetica-Bold", 36)
    c.drawCentredString(420, 400, "Certificate of Completion")
    
    c.setFont("Helvetica", 24)
    c.drawCentredString(420, 300, f"Presented to {name}")
    
    c.setFont("Helvetica", 18)
    c.drawCentredString(420, 250, "For successfully completing the course")
    
    c.save()

generate_certificate("Siddharth")
