from app import create_app
from app.configuracion_base import db

app = create_app()

with app.app_context():
    db.create_all()
    print("Base de datos inicializada.")
 