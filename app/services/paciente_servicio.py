from app.repositories.paciente_repository import PacienteRepository
from app.model.paciente import Paciente
#Servicios de la API
class PacienteService:
    #Muestra los pacientes
    @staticmethod
    def listar():
        return PacienteRepository.obtener_todos()
    #Crea un paciente
    @staticmethod
    def crear(data):
        paciente = Paciente(**data)
        return PacienteRepository.crear(paciente)
