from app import db
from app.model.cita import Cita

class CitaRepository:
    @staticmethod
    def obtener_todos():
        return Cita.query.all()

    @staticmethod
    def obtener_por_id(id):
        return Cita.query.get(id)

    @staticmethod
    def crear(cita):
        db.session.add(cita)
        db.session.commit()
        return cita

    @staticmethod
    def actualizar(id, data):
        cita = Cita.query.get(id)
        if not cita:
            return None
        for key, value in data.items():
            setattr(cita, key, value)
        db.session.commit()
        return cita

    @staticmethod
    def eliminar(id):
        cita = Cita.query.get(id)
        if not cita:
            return None
        db.session.delete(cita)
        db.session.commit()
        return cita
