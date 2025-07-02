from flask_restx import Namespace, Resource, fields
from flask import request
from app.services import caja_diaria_servicio

api = Namespace('caja', description='Operaciones de caja diaria')

modelo_fecha = api.model('FechaCaja', {
    'fecha': fields.String(required=True, example="2025-07-02")
})

modelo_respuesta = api.model('CajaRespuesta', {
    'fecha': fields.String,
    'monto_total': fields.Float
})

@api.route('/')
class CajaGenerar(Resource):
    @api.expect(modelo_fecha)
    @api.marshal_with(modelo_respuesta)
    def post(self):
        data = request.json
        monto = caja_diaria_servicio.generar_caja_diaria(data['fecha'])
        return {"fecha": data['fecha'], "monto_total": monto}, 201

    @api.marshal_list_with(modelo_respuesta)
    def get(self):
        cajas = caja_diaria_servicio.obtener_cajas()
        return [{"fecha": str(caja.fecha), "monto_total": caja.monto_total} for caja in cajas]
