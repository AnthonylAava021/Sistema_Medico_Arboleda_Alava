from app import db
#Creación de la tabla de paciente con sus campos
class Paciente(db.Model):
    __tablename__ = 'pacientes'#Nombre de la tabla
    #Campos de la tabla paciente
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    cedula = db.Column(db.String(20), unique=True, nullable=False)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(100))
    historial_medico = db.Column(db.String(100))
    fecha_nacimiento = db.Column(db.String(100))
    
