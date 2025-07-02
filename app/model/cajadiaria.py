from app.configuracion_base import db
from datetime import date

class CajaDiaria(db.Model):
    __tablename__ = 'caja_diaria'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, default=date.today, unique=True, nullable=False)
    monto_total = db.Column(db.Float, nullable=False)
