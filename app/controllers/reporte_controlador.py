from flask_restx import Namespace, Resource
from app.services import reporte_servicio

api = Namespace('reportes', description='Reporte general de ventas')

@api.route('/')
class ReporteBalance(Resource):
    def get(self):
        reporte = reporte_servicio.obtener_balance_general()
        return reporte, 200
