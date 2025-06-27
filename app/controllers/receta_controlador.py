from flask_restx import Namespace, Resource, fields
from flask import request
from app.services import receta_servicio

api = Namespace('recetas', description='Gestión de recetas médicas')

receta_model = api.model('Receta', {
    'medicamento': fields.String(required=True),
    'dosis': fields.String(required=True),
    'instrucciones': fields.String,
    'consulta_id': fields.Integer(required=True)
})

@api.route('/')
class RecetaLista(Resource):
    @api.expect(receta_model)
    @api.marshal_with(receta_model, code=201)
    def post(self):
        """Registrar una receta médica asociada a una consulta"""
        data = request.json
        return receta_servicio.crear_receta(data), 201

@api.route('/consulta/<int:consulta_id>')
class RecetaConsulta(Resource):
    @api.marshal_with(receta_model)
    def get(self, consulta_id):
        """Obtener la receta asociada a una consulta"""
        return receta_servicio.obtener_receta_por_consulta(consulta_id)
