from app.configuracion_base import db

class Cita(db.Model):
    __tablename__ = 'citas'

    id = db.Column(db.Integer, primary_key=True)
    fecha_hora = db.Column(db.DateTime, nullable=False)
    estado = db.Column(db.String(20), nullable=False, default='pendiente')
    motivo = db.Column(db.String(255), nullable=True)

    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctores.id'), nullable=False)

    paciente = db.relationship('Paciente', backref='citas', lazy=True)
    doctor = db.relationship('Doctor', backref='citas', lazy=True)
