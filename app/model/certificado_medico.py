from app.configuracion_base import db
from datetime import datetime, timedelta

class CertificadoMedico(db.Model):
    __tablename__ = 'certificados_medicos'

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    fecha_emision = db.Column(db.DateTime, default=datetime.utcnow)

    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctores.id'), nullable=False)
    cita_id = db.Column(db.Integer, db.ForeignKey('citas.id'), nullable=True)

    paciente = db.relationship("Paciente", backref="certificados")
    doctor = db.relationship("Doctor", backref="certificados")
    cita = db.relationship("Cita", backref="certificados")

    def es_vigente(self):
        return datetime.utcnow() <= self.fecha_emision + timedelta(days=7)
