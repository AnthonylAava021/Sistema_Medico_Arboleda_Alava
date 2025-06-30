from app import db
from datetime import datetime

class Reporte(db.Model):
    __tablename__ = 'reportes'
    
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    fecha_generacion = db.Column(db.DateTime, default=datetime.utcnow)
    parametros = db.Column(db.JSON)  # Para almacenar los parámetros del reporte
    
    @staticmethod
    def generar_historial_clinico(paciente_id):
        # Implementación para generar PDF del historial clínico
        pass
    
    @staticmethod
    def filtrar_ventas(fecha_inicio, fecha_fin):
        return Factura.query.filter(
            Factura.fecha >= fecha_inicio,
            Factura.fecha <= fecha_fin
        ).all()
