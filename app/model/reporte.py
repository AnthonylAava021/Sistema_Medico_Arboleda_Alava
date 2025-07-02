# app/models/reporte.py
from app.configuracion_base import db

class Reporte(db.Model):
    __tablename__ = 'reportes'
    id = db.Column(db.Integer, primary_key=True)
