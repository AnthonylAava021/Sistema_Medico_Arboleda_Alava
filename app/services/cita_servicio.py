from datetime import datetime
from app.model.cita import Cita
from app.configuracion_base import db

def registrar_cita(data):
    nueva_cita = Cita(
        fecha_hora=datetime.fromisoformat(data['fecha_hora']),
        estado=data.get('estado', 'pendiente'),
        motivo=data.get('motivo'),
        paciente_id=data['paciente_id'],
        doctor_id=data['doctor_id']
    )
    db.session.add(nueva_cita)
    db.session.commit()
    return nueva_cita

def listar_citas():
    return Cita.query.all()

def buscar_cita_por_id(cita_id):
    return Cita.query.get(cita_id)
