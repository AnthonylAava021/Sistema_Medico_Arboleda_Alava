from flask_restx import Namespace, Resource, fields
from app.services.cita_servicio import CitaService

api = Namespace('citas', description='Operaciones con citas')

# Modelo que representa la estructura de una cita
modelo_cita = api.model('Cita', {
    'fecha_hora': fields.DateTime(required=True, description="Fecha y hora de la cita"),
    'estado': fields.String(required=True, description="Estado de la cita (pendiente, completada, cancelada)"),
    'motivo': fields.String(required=True, description="Motivo de la cita"),
    'paciente_id': fields.Integer(required=True, description="ID del paciente"),
    'doctor_id': fields.Integer(required=True, description="ID del doctor")
})

# Endpoints para listar y crear citas
@api.route('/')
class CitaList(Resource):

    @api.marshal_list_with(modelo_cita)
    def get(self):
        """Listar todas las citas"""
        return CitaService.listar()

    @api.expect(modelo_cita)
    @api.marshal_with(modelo_cita, code=201)
    def post(self):
        """Crear una nueva cita"""
        return CitaService.crear(api.payload), 201


# Endpoints para obtener, actualizar y eliminar una cita por ID
@api.route('/<int:id>')
@api.response(404, 'Cita no encontrada')
class CitaResource(Resource):

    @api.marshal_with(modelo_cita)
    def get(self, id):
        """Obtener una cita por ID"""
        return CitaService.obtener(id)

    @api.expect(modelo_cita)
    @api.marshal_with(modelo_cita)
    def put(self, id):
        """Actualizar una cita"""
        return CitaService.actualizar(id, api.payload)

    @api.response(204, 'Cita eliminada')
    def delete(self, id):
        """Eliminar una cita"""
        CitaService.eliminar(id)
        return '', 204
