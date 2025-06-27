from app.configuracion_base import db
from datetime import datetime

class Consulta(db.Model):
    __tablename__ = 'consultas'

    id = db.Column(db.Integer, primary_key=True)
    diagnostico = db.Column(db.String(255), nullable=False)
    notas = db.Column(db.Text, nullable=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctores.id'), nullable=False)

    paciente = db.relationship('Paciente', backref='consultas', lazy=True)
    doctor = db.relationship('Doctor', backref='consultas', lazy=True)
