from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager
from app.configuracion_base import db  
from .medico import CertificadoMedico
from .factura import Factura, MetodoPago
from .caja import DiarioCaja
from .reporte import Reporte
from .plan_cuentas import PlanCuentas

__all__ = ['CertificadoMedico', 'Factura', 'MetodoPago', 'DiarioCaja', 'Reporte', 'PlanCuentas']

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app) 

    JWTManager(app)

    api = Api(app, version='1.0', title='API Citas Médicas', description='Sistema de Gestión de Citas Médicas', doc='/docs')

    from app.controllers.paciente_controlador import api as paciente_ns
    from app.controllers.usuario_controlador import api as usuario_ns
    from app.controllers.doctor_controlador import api as doctor_ns
    from app.controllers.cita_controlador import api as cita_ns
    from app.controllers.consulta_controlador import api as consulta_ns
    from app.controllers.receta_controlador import api as receta_ns
   

    api.add_namespace(paciente_ns)
    api.add_namespace(usuario_ns)
    api.add_namespace(doctor_ns)
    api.add_namespace(cita_ns)
    api.add_namespace(consulta_ns)
    api.add_namespace(receta_ns)

    return app
