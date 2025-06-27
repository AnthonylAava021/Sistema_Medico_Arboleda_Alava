from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager
from app.configuracion_base import db  

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
   

    api.add_namespace(paciente_ns)
    api.add_namespace(usuario_ns)
    api.add_namespace(doctor_ns)
    api.add_namespace(cita_ns)

    return app
