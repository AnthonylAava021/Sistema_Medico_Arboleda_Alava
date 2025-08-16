from app.model.doctor import Doctor
from app import db

class DoctorRepository:
    # Obtener todos los doctores
    @staticmethod
    def obtener_todos():
        return Doctor.query.all()

    # Crear un doctor
    @staticmethod
    def crear(doctor):
        db.session.add(doctor)
        db.session.commit()
        return doctor

    # Obtener un doctor por ID
    @staticmethod
    def obtener_por_id(id):
        return Doctor.query.get(id)

    # Actualizar un doctor
    @staticmethod
    def actualizar(id, data):
        doctor = Doctor.query.get(id)
        if not doctor:
            return None
        for key, value in data.items():
            setattr(doctor, key, value)
        db.session.commit()
        return doctor

    # Eliminar un doctor
    @staticmethod
    def eliminar(id):
        doctor = Doctor.query.get(id)
        if not doctor:
            return None
        db.session.delete(doctor)
        db.session.commit()
        return doctor
