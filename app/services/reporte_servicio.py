
from app.model.cajadiaria import CajaDiaria
from app.configuracion_base import db

def obtener_balance_general():
    cajas = db.session.query(CajaDiaria).all()
    total_general = sum(caja.monto_total for caja in cajas)
    detalle = [{"fecha": str(caja.fecha), "monto": caja.monto_total} for caja in cajas]
    
    return {
        "total_general": total_general,
        "detalle_por_dia": detalle
    }
