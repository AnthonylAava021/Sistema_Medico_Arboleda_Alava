from enum import Enum
from app import db

class MetodoPago(Enum):
    EFECTIVO = 'Efectivo'
    TARJETA = 'Tarjeta'
    TRANSFERENCIA = 'Transferencia'

class Factura(db.Model):
    __tablename__ = 'facturas'
    
    id = db.Column(db.Integer, primary_key=True)
    monto = db.Column(db.Float, nullable=False)
    estado = db.Column(db.String(20), default='Pendiente')
    fecha = db.Column(db.Date, default=datetime.utcnow)
    metodo_pago = db.Column(db.String(20))
    consulta_id = db.Column(db.Integer, db.ForeignKey('consultas.id'))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    
    def calcular_total(self, iva=0.16):
        return self.monto * (1 + iva)
    
    def emitir_comprobante(self):
        # Implementación para generar comprobante
        pass
    
    def registrar_pago(self, metodo):
        self.metodo_pago = metodo.value if isinstance(metodo, MetodoPago) else metodo
        self.estado = 'Pagado'
        db.session.commit()
