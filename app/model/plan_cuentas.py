from app import db

class PlanCuentas(db.Model):
    __tablename__ = 'plan_cuentas'
    
    id = db.Column(db.Integer, primary_key=True)
    codigo_cuenta = db.Column(db.String(20), unique=True, nullable=False)
    nombre_cuenta = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)  # Activo, Pasivo, Patrimonio, etc.
    
    def clasificar_transaccion(self, transaccion):
        transaccion.cuenta_id = self.id
        db.session.commit()
    
    @staticmethod
    def generar_balance():
        cuentas = PlanCuentas.query.all()
        balance = {}
        
        for cuenta in cuentas:
            total = sum(
                mov.monto for mov in DiarioCaja.query.filter_by(cuenta_id=cuenta.id).all()
            )
            balance[cuenta.nombre_cuenta] = total
        
        return balance