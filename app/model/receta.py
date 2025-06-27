from app.configuracion_base import db

class Receta(db.Model):
    __tablename__ = 'recetas'

    id = db.Column(db.Integer, primary_key=True)
    medicamento = db.Column(db.String(100), nullable=False)
    dosis = db.Column(db.String(100), nullable=False)
    instrucciones = db.Column(db.Text, nullable=True)

    consulta_id = db.Column(db.Integer, db.ForeignKey('consultas.id'), nullable=False, unique=True)

    consulta = db.relationship('Consulta', backref=db.backref('receta', uselist=False), lazy=True)
