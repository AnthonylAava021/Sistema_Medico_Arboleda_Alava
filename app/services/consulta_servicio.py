from datetime import datetime
from app.model.consulta import Consulta
from app.configuracion_base import db

def registrar_consulta(data):
    nueva = Consulta(
        diagnostico=data['diagnostico'],
        notas=data.get('notas'),
        receta=data.get('receta'),
        fecha=datetime.fromisoformat(data['fecha']),
        paciente_id=data['paciente_id'],
        doctor_id=data['doctor_id']
    )
    db.session.add(nueva)
    db.session.commit()
    return nueva

def listar_consultas():
    return Consulta.query.all()

def obtener_consulta_por_id(consulta_id):
    return Consulta.query.get(consulta_id)
