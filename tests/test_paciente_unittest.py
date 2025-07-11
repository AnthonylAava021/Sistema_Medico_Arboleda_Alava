import unittest
from app import db
from app.model.paciente import Paciente
from flask import Flask

class TestPacienteModel(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['TESTING'] = True
        db.init_app(self.app)

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_creacion_paciente(self):
        with self.app.app_context():
            paciente = Paciente(
                nombre="Juan Perez",
                genero="Masculino",
                cedula="1234567890",
                telefono="0987654321",
                direccion="Calle Falsa 123",
                historial_medico="Sin antecedentes",
                fecha_nacimiento="1990-01-01"
            )
            db.session.add(paciente)
            db.session.commit()

            resultado = Paciente.query.filter_by(cedula="1234567890").first()
            self.assertIsNotNone(resultado)
            self.assertEqual(resultado.nombre, "Juan Perez")

if __name__ == '__main__':
    unittest.main()
