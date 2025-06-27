from app.model.cita import Cita
from app.configuracion_base import db

def guardar_cita(cita):
    db.session.add(cita)
    db.session.commit()
    return cita

def obtener_citas():
    return Cita.query.all()

def obtener_cita_por_id(cita_id):
    return Cita.query.get(cita_id)
