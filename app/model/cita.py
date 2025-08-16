from app import db

class Cita(db.Model):
    __tablename__ = 'citas'  # Nombre de la tabla en la BD

    id = db.Column(db.Integer, primary_key=True)
    fecha_hora = db.Column(db.DateTime, nullable=False)
    estado = db.Column(db.String(20), nullable=False)
    motivo = db.Column(db.String(255), nullable=False)

    # Llaves foráneas
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctores.id'), nullable=False)

    # Relaciones (opcional, para poder acceder desde la cita al paciente/doctor directamente)
    paciente = db.relationship("Paciente", backref="citas", lazy=True)
    doctor = db.relationship("Doctor", backref="citas", lazy=True)
