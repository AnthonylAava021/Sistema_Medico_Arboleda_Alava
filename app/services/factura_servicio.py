from app.model.factura import Factura
from app.model.paciente import Paciente
from app.configuracion_base import db
from flask import abort

def crear_factura(data):
    # Buscar paciente por número de cédula
    paciente = Paciente.query.filter_by(cedula=data['cedula']).first()

    if not paciente:
        abort(404, description="Paciente no encontrado")

    factura = Factura(
        monto=data['monto'],
        metodo_pago=data['metodo_pago'],
        estado='pagado',
        paciente_id=paciente.id,
        cita_id=data['cita_id']
    )
    db.session.add(factura)
    db.session.commit()
    return factura

def obtener_facturas():
    return Factura.query.all()
