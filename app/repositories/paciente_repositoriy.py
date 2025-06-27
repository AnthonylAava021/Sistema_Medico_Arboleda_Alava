from app.model.paciente import Paciente
from app import db

class PacienteRepository:
#Metodo para obtener todos los pacientes
    @staticmethod
    def obtener_todos():
        return Paciente.query.all()
#Método para obtener los pacientes
    @staticmethod
    def crear(paciente):
        db.session.add(paciente)
        db.session.commit()
        return paciente
