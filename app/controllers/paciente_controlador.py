from flask_restx import Namespace, Resource, fields
from app.services.paciente_servicio import PacienteService

api = Namespace('pacientes', description='Operaciones con pacientes')
#Se establece el modelo que tendrá los pacientes
modelo_paciente = api.model('Paciente', {
    'nombre': fields.String(required=True),
    'cedula': fields.String(required=True),
    'telefono': fields.String,
    'genero':fields.String(required=True),
    'direccion' : fields.String,
    'historial_medico' : fields.String,
    'fecha_nacimiento' : fields.String


})
#Asignación de las rutas o endpoints
@api.route('/')
class PacienteList(Resource):

    @api.marshal_list_with(modelo_paciente)
    def get(self):
        return PacienteService.listar()

    @api.expect(modelo_paciente)
    @api.marshal_with(modelo_paciente, code=201)
    def post(self):
        return PacienteService.crear(api.payload), 201

@api.route('/<int:id>')
@api.response(404, 'Paciente no encontrado')
class PacienteResource(Resource):

    @api.marshal_with(modelo_paciente)
    def get(self, id):
        """Obtener un paciente por ID"""
        return PacienteService.obtener(id)

    @api.expect(modelo_paciente)
    @api.marshal_with(modelo_paciente)
    def put(self, id):
        """Actualizar paciente"""
        return PacienteService.actualizar(id, api.payload)

    @api.response(204, 'Paciente eliminado')
    def delete(self, id):
        """Eliminar paciente"""
        PacienteService.eliminar(id)
        return '', 204

