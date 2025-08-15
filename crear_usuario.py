from app import create_app
from app.configuracion_base import db
from app.model.usuario import Usuario, UserRole
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    # Crear nuevo usuario admin
    nuevo_admin = Usuario(
        username="admin",
        email="admin@test.com",
        password_hash=generate_password_hash("1234"),
        role=UserRole.ADMIN
    )
    db.session.add(nuevo_admin)
    db.session.commit()
    print("Usuario 'admin' creado ")
