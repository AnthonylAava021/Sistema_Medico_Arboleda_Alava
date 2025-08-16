from app.repositories.doctor_repository import DoctorRepository
from app.model.doctor import Doctor

class DoctorService:
    @staticmethod
    def listar():
        return DoctorRepository.obtener_todos()

    @staticmethod
    def crear(data):
        doctor = Doctor(**data)
        return DoctorRepository.crear(doctor)

    @staticmethod
    def obtener(id):
        return DoctorRepository.obtener_por_id(id)

    @staticmethod
    def actualizar(id, data):
        return DoctorRepository.actualizar(id, data)

    @staticmethod
    def eliminar(id):
        return DoctorRepository.eliminar(id)
