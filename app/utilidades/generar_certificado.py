from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def generar_pdf_certificado(certificado):
    carpeta = "pdf_certificados"
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    ruta_pdf = os.path.join(carpeta, f"certificado_{certificado.id}.pdf")
    c = canvas.Canvas(ruta_pdf, pagesize=letter)

    c.setFont("Helvetica", 14)
    c.drawString(50, 750, "CERTIFICADO MÉDICO")
    c.setFont("Helvetica", 12)
    c.drawString(50, 720, f"Tipo: {certificado.tipo}")
    c.drawString(50, 700, f"Emitido por el Dr./Dra.: {certificado.doctor.nombre}")
    c.drawString(50, 680, f"A nombre de: {certificado.paciente.nombre}")
    c.drawString(50, 660, f"Fecha de emisión: {certificado.fecha_emision.strftime('%Y-%m-%d')}")
    
    text_obj = c.beginText(50, 640)
    text_obj.textLines(f"Descripción:\n{certificado.descripcion}")
    c.drawText(text_obj)

    c.save()
