from app.model.doctor import Doctor
from app.configuracion_base import db

def crear_doctor(doctor):
    db.session.add(doctor)
    db.session.commit()
    return doctor

def obtener_todos_los_doctores():
    return Doctor.query.all()

def obtener_doctor_por_id(doctor_id):
    return Doctor.query.get(doctor_id)
