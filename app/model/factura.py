from app.configuracion_base import db

class Factura(db.Model):
    __tablename__ = 'facturas'

    id = db.Column(db.Integer, primary_key=True)
    monto = db.Column(db.Float, nullable=False)
    estado = db.Column(db.String(20), default='pagado')
    fecha = db.Column(db.DateTime, default=db.func.current_timestamp())
    metodo_pago = db.Column(db.String(50), nullable=False)
    
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)
    cita_id = db.Column(db.Integer, db.ForeignKey('citas.id'), nullable=False)

    paciente = db.relationship('Paciente', backref='facturas')
