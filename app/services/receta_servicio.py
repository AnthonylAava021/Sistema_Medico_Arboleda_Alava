from app.model.receta import Receta
from app.configuracion_base import db

def crear_receta(data):
    nueva = Receta(
        medicamento=data['medicamento'],
        dosis=data['dosis'],
        instrucciones=data.get('instrucciones'),
        consulta_id=data['consulta_id']
    )
    db.session.add(nueva)
    db.session.commit()
    return nueva

def obtener_receta_por_consulta(consulta_id):
    return Receta.query.filter_by(consulta_id=consulta_id).first()
