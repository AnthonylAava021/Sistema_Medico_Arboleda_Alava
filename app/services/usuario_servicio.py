from app.repositories.usuario_repositorio import get_usuario_por_username, get_usuario_por_email, crear_usuario
from app.model.usuario import Usuario, UserRole
from flask_jwt_extended import create_access_token #Instalar dependecia con pip install flask_jwt_extended

def registrar_usuario(username, email, password, role_str):
    if get_usuario_por_username(username) or get_usuario_por_email(email):
        raise ValueError("Usuario o email ya registrado")
    
    usuario = Usuario(
        username=username,
        email=email,
        role=UserRole(role_str)
    )
    usuario.set_password(password)
    return crear_usuario(usuario)

def login_usuario(username, password):
    usuario = get_usuario_por_username(username)
    if not usuario or not usuario.check_password(password):
        return None
    access_token = create_access_token(identity=usuario.id)
    return access_token
