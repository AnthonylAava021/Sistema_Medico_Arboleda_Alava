from datetime import datetime
from app import db

class CertificadoMedico(db.Model):
    __tablename__ = 'certificados_medicos'
    
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    fecha_emision = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    medico_id = db.Column(db.Integer, db.ForeignKey('medicos.id'), nullable=False)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)
    
    def validar_vigencia(self, fecha):
        return fecha <= self.fecha_emision
    
    def generar_pdf(self):

        pass