from app.repositories.cita_repository import CitaRepository
from app.model.cita import Cita

# Servicios de la API
class CitaService:
    # Muestra todas las citas
    @staticmethod
    def listar():
        return CitaRepository.obtener_todos()

    # Crea una cita
    @staticmethod
    def crear(data):
        cita = Cita(**data)
        return CitaRepository.crear(cita)

    @staticmethod
    def obtener_por_id(id):
        return CitaRepository.obtener_por_id(id)

    @staticmethod
    def actualizar(id, data):
        return CitaRepository.actualizar(id, data)

    @staticmethod
    def eliminar(id):
        return CitaRepository.eliminar(id)
