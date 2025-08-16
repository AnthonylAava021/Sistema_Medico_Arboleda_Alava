from flask_restx import Namespace, Resource, fields
from app.services.doctor_servicio import DoctorService

api = Namespace('doctores', description='Operaciones con doctores')

modelo_doctor = api.model('Doctor', {
    'nombre': fields.String(required=True),
    'cedula': fields.String(required=True),
    'genero': fields.String(required=True),
    'especialidad': fields.String(required=True),
    'telefono': fields.String,
    'cargo': fields.String(required=True),
})

@api.route('/')
class DoctorList(Resource):

    @api.marshal_list_with(modelo_doctor)
    def get(self):
        return DoctorService.listar()

    @api.expect(modelo_doctor)
    @api.marshal_with(modelo_doctor, code=201)
    def post(self):
        return DoctorService.crear(api.payload), 201

@api.route('/<int:id>')
@api.response(404, 'Doctor no encontrado')
class DoctorResource(Resource):

    @api.marshal_with(modelo_doctor)
    def get(self, id):
        """Obtener un doctor por ID"""
        return DoctorService.obtener(id)

    @api.expect(modelo_doctor)
    @api.marshal_with(modelo_doctor)
    def put(self, id):
        """Actualizar doctor"""
        return DoctorService.actualizar(id, api.payload)

    @api.response(204, 'Doctor eliminado')
    def delete(self, id):
        """Eliminar doctor"""
        DoctorService.eliminar(id)
        return '', 204
