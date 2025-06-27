from flask_restx import Namespace, Resource, fields
from flask import request
from app.services import consulta_servicio

api = Namespace('consultas', description='Gestión de consultas médicas')

consulta_model = api.model('Consulta', {
    'diagnostico': fields.String(required=True),
    'notas': fields.String,
    'receta': fields.String,
    'fecha': fields.String(required=True, description="Formato ISO 8601"),
    'paciente_id': fields.Integer(required=True),
    'doctor_id': fields.Integer(required=True)
})

@api.route('/')
class ConsultaLista(Resource):
    @api.marshal_list_with(consulta_model)
    def get(self):
        """Listar todas las consultas"""
        return consulta_servicio.listar_consultas()

    @api.expect(consulta_model)
    @api.marshal_with(consulta_model, code=201)
    def post(self):
        """Registrar una nueva consulta médica"""
        data = request.json
        return consulta_servicio.registrar_consulta(data), 201
