import os
from flask import abort, request, send_file
from flask_restx import Namespace, Resource, fields
from app.services import certificado_medico_servicio

api = Namespace('certificados', description='Operaciones relacionadas con certificados médicos')

modelo_certificado = api.model('Certificado', {
    'tipo': fields.String(required=True),
    'descripcion': fields.String(required=True),
    'paciente_id': fields.Integer(required=True),
    'doctor_id': fields.Integer(required=True),
    'cita_id': fields.Integer(required=False)
})

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))  # Directorio base del proyecto
RUTA_CERTIFICADOS = os.path.join(BASE_DIR, 'pdf_certificados')          # Ruta absoluta a pdf_certificados

@api.route('/')
class CertificadoResource(Resource):
    @api.expect(modelo_certificado)
    def post(self):
        data = request.json
        certificado = certificado_medico_servicio.crear_certificado(data)
        return {"message": "Certificado creado", "id": certificado.id}, 201

@api.route('/<int:certificado_id>/descargar')
class DescargarCertificado(Resource):
    def get(self, certificado_id):
        ruta = os.path.join(RUTA_CERTIFICADOS, f"certificado_{certificado_id}.pdf")
        
        if not os.path.exists(ruta):
            abort(404, description="Certificado no encontrado o no generado aún.")
        
        return send_file(ruta, as_attachment=True)
