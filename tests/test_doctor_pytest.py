from app.model.doctor import Doctor
from app import db

def test_insertar_doctor(app):
    with app.app_context():
        doctor = Doctor(
            nombre="Dra. María Pérez",
            cedula="0987654321",
            genero="Femenino",
            especialidad="Pediatría",
            telefono="0999999999",
            cargo="Pediatra"
        )
        db.session.add(doctor)
        db.session.commit()

        resultado = Doctor.query.filter_by(cedula="0987654321").first()
        assert resultado is not None
        assert resultado.nombre == "Dra. María Pérez"
