from app.model.doctor import Doctor
from app.repositories.doctor_repositorio import crear_doctor, obtener_todos_los_doctores, obtener_doctor_por_id

def registrar_doctor(data):
    nuevo_doctor = Doctor(
        nombre=data['nombre'],
        cedula=data['cedula'],
        genero=data['genero'],
        especialidad=data['especialidad'],
        telefono=data.get('telefono'),
        cargo=data['cargo']
    )
    return crear_doctor(nuevo_doctor)

def listar_doctores():
    return obtener_todos_los_doctores()

def buscar_doctor_por_id(doctor_id):
    return obtener_doctor_por_id(doctor_id)
