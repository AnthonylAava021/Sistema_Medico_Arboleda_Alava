from app import db

class Doctor(db.Model):
    __tablename__ = 'doctores'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    cedula = db.Column(db.String(20), unique=True, nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    especialidad = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20))
    cargo = db.Column(db.String(50), nullable=False)
