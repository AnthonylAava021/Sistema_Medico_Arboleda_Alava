from flask_restx import Namespace, Resource, fields
from flask import request
from app.services import cita_servicio

api = Namespace('citas', description='Gestión de citas médicas')

cita_model = api.model('Cita', {
    'fecha_hora': fields.String(required=True, description="Formato ISO 8601"),
    'estado': fields.String(required=False, default='pendiente'),
    'motivo': fields.String(required=False),
    'paciente_id': fields.Integer(required=True),
    'doctor_id': fields.Integer(required=True),
})

@api.route('/')
class CitaLista(Resource):
    @api.marshal_list_with(cita_model)
    def get(self):
        """Listar todas las citas"""
        return cita_servicio.listar_citas()

    @api.expect(cita_model)
    @api.marshal_with(cita_model, code=201)
    def post(self):
        """Registrar una nueva cita"""
        data = request.json
        return cita_servicio.registrar_cita(data), 201
