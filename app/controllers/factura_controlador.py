from flask import request
from flask_restx import Namespace, Resource, fields, marshal_with
from app.services import factura_servicio
from app.model.factura import Factura

api = Namespace('facturas', description='Gestión de facturas médicas')

modelo_factura_post = api.model('FacturaPost', {
    'cedula': fields.String(required=True),
    'monto': fields.Float(required=True),
    'metodo_pago': fields.String(required=True),
    'cita_id': fields.Integer(required=True)
})

modelo_factura_get = api.model('FacturaGet', {
    'id': fields.Integer,
    'monto': fields.Float,
    'estado': fields.String,
    'fecha': fields.DateTime,
    'metodo_pago': fields.String,
    'cita_id': fields.Integer,
    'paciente': fields.String
})

@api.route('/')
class FacturaResource(Resource):
    @api.expect(modelo_factura_post)
    def post(self):
        data = request.json
        factura = factura_servicio.crear_factura(data)
        return {"message": "Factura creada", "id": factura.id}, 201

    @api.marshal_with(modelo_factura_get, as_list=True)
    def get(self):
        facturas = factura_servicio.obtener_facturas()
        resultado = []
        for f in facturas:
            resultado.append({
                'id': f.id,
                'monto': f.monto,
                'estado': f.estado,
                'fecha': f.fecha,
                'metodo_pago': f.metodo_pago,
                'cita_id': f.cita_id,
                'paciente': f.paciente.nombre + " - " + f.paciente.cedula
            })
        return resultado
