from app.model.cajadiaria import CajaDiaria
from app.model.factura import Factura
from app.configuracion_base import db
from datetime import datetime, timedelta

def generar_caja_diaria(fecha_str):
    try:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Formato de fecha inválido. Usa YYYY-MM-DD.")

    inicio = datetime(fecha.year, fecha.month, fecha.day)
    fin = inicio + timedelta(days=1)

    total = db.session.query(db.func.sum(Factura.monto)) \
        .filter(Factura.fecha >= inicio, Factura.fecha < fin) \
        .scalar() or 0.0

    # Verificar si ya existe una caja para ese día
    caja_existente = CajaDiaria.query.filter_by(fecha=fecha).first()
    if caja_existente:
        caja_existente.monto_total = total
    else:
        caja = CajaDiaria(fecha=fecha, monto_total=total)
        db.session.add(caja)

    db.session.commit()
    return total

def obtener_cajas():
    return CajaDiaria.query.order_by(CajaDiaria.fecha.desc()).all()
