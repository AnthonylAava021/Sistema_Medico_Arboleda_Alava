import sys
import os

# Agregar la carpeta raíz del proyecto al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from app.configuracion_base import db
from app.models.usuario import Usuario

# Inicializar app y contexto
app = create_app()
app.app_context().push()

# Configura los datos del nuevo usuario aquí
USERNAME = "nuevo_usuario"       # Cambia por el nombre de usuario que quieras
EMAIL = "usuario@correo.com"     # Cambia por el correo del usuario
PASSWORD = "1234"                # Cambia por la contraseña
ROLE = "PACIENTE"                # PACIENTE, MEDICO, RECEPCIONISTA, ADMIN

# Crear el usuario
nuevo_usuario = Usuario(
    username=USERNAME,
    email=EMAIL,
    role=ROLE
)
nuevo_usuario.set_password(PASSWORD)

# Guardar en la base de datos
db.session.add(nuevo_usuario)
db.session.commit()

print(f"Usuario '{USERNAME}' creado correctamente con rol '{ROLE}'.")
