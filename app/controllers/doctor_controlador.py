from flask_restx import Namespace, Resource, fields
from flask import request
from app.services import doctor_servicio

api = Namespace('doctores', description='Operaciones relacionadas con los doctores')

doctor_model = api.model('Doctor', {
    'nombre': fields.String(required=True),
    'cedula': fields.String(required=True),
    'genero': fields.String(required=True),
    'especialidad': fields.String(required=True),
    'telefono': fields.String(required=False),
    'cargo': fields.String(required=True),
})

@api.route('/')
class DoctorLista(Resource):
    @api.marshal_list_with(doctor_model)
    def get(self):
        """Listar todos los doctores"""
        return doctor_servicio.listar_doctores()

    @api.expect(doctor_model)
    @api.marshal_with(doctor_model, code=201)
    def post(self):
        """Registrar un nuevo doctor"""
        data = request.json
        return doctor_servicio.registrar_doctor(data), 201
