import os
from datetime import datetime
from app.model.certificado_medico import CertificadoMedico
from app.configuracion_base import db
from app.utilidades.generar_certificado import generar_pdf_certificado

def crear_certificado(data):
    nuevo = CertificadoMedico(
        tipo=data['tipo'],
        descripcion=data['descripcion'],
        fecha_emision=datetime.utcnow(),
        paciente_id=data['paciente_id'],
        doctor_id=data['doctor_id'],
        cita_id=data.get('cita_id')
    )
    db.session.add(nuevo)
    db.session.commit()

    generar_pdf_certificado(nuevo)
    return nuevo

def obtener_certificado(certificado_id):
    return CertificadoMedico.query.get(certificado_id)
