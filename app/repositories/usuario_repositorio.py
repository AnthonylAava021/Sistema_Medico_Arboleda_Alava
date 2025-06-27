from app.model.usuario import Usuario
from app.configuracion_base import db

def get_usuario_por_username(username):
    return Usuario.query.filter_by(username=username).first()

def get_usuario_por_email(email):
    return Usuario.query.filter_by(email=email).first()

def crear_usuario(usuario):
    db.session.add(usuario)
    db.session.commit()
    return usuario
