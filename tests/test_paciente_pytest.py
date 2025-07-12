from app.model.paciente import Paciente
from app import db

def test_insertar_paciente(app):
    with app.app_context():
        paciente = Paciente(
            nombre="Ana Torres",
            genero="Femenino",
            cedula="0987654321",
            telefono="0999999999",
            direccion="Av. Libertad",
            historial_medico="Alergia",
            fecha_nacimiento="1985-10-10"
        )
        db.session.add(paciente)
        db.session.commit()

        resultado = Paciente.query.filter_by(cedula="0987654321").first()
        assert resultado is not None
        assert resultado.nombre == "Ana Torres"
