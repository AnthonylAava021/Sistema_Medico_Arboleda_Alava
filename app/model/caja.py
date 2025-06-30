from app import db

class DiarioCaja(db.Model):
    __tablename__ = 'diario_caja'
    
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    descripcion = db.Column(db.String(200), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    tipo = db.Column(db.String(10), nullable=False)  # 'INGRESO' o 'EGRESO'
    factura_id = db.Column(db.Integer, db.ForeignKey('facturas.id'))
    cuenta_id = db.Column(db.Integer, db.ForeignKey('plan_cuentas.id'))
    
    @classmethod
    def registrar_movimiento(cls, descripcion, monto, tipo, factura_id=None, cuenta_id=None):
        movimiento = cls(
            descripcion=descripcion,
            monto=monto,
            tipo=tipo,
            factura_id=factura_id,
            cuenta_id=cuenta_id
        )
        db.session.add(movimiento)
        db.session.commit()
        return movimiento