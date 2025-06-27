from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)

    api = Api(app, version='1.0', title='API Citas Médicas', description='Sistema de Gestión de Citas Médicas', doc='/docs')

    # Importar namespaces
    from app.controllers.paciente_controlador import api as paciente_ns
    from app.controllers.cita_controlador import api as cita_ns

    api.add_namespace(paciente_ns)
    api.add_namespace(cita_ns)

    return app