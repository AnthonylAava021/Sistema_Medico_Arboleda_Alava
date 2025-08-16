from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from app.configuracion_base import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Evitar redirect por barra final
    app.url_map.strict_slashes = False

    # ✅ CORS correcto (solo aquí)
    CORS(
        app,
        resources={r"/*": {"origins": "http://localhost:3000"}},
        supports_credentials=True,
        allow_headers=["Content-Type", "Authorization"],
        methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    )

    # Extensiones
    db.init_app(app)
    JWTManager(app)

    # API /docs
    api = Api(
        app,
        version='1.0',
        title='API Citas Médicas',
        description='Sistema de Gestión de Citas Médicas',
        doc='/docs'
    )

    # Namespaces
    from app.controllers.paciente_controlador import api as paciente_ns
    from app.controllers.usuario_controlador import api as usuario_ns
    from app.controllers.doctor_controlador import api as doctor_ns
    from app.controllers.cita_controlador import api as cita_ns
    from app.controllers.consulta_controlador import api as consulta_ns
    from app.controllers.receta_controlador import api as receta_ns
    from app.controllers.certificado_medico_controlador import api as certificado_ns
    from app.controllers.factura_controlador import api as factura_ns
    from app.controllers.caja_diaria_controlador import api as cajadiaria_ns
    from app.controllers.reporte_controlador import api as reporte_ns

    api.add_namespace(paciente_ns)
    api.add_namespace(usuario_ns)
    api.add_namespace(doctor_ns)
    api.add_namespace(cita_ns)          # 👈 importante
    api.add_namespace(consulta_ns)
    api.add_namespace(receta_ns)
    api.add_namespace(certificado_ns)
    api.add_namespace(factura_ns)
    api.add_namespace(cajadiaria_ns)
    api.add_namespace(reporte_ns)

    return app
