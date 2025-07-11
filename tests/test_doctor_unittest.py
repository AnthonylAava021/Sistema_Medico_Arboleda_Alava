import unittest
from flask import Flask
from app.configuracion_base import db
from app.model.doctor import Doctor

class TestDoctorModel(unittest.TestCase):
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

    def test_creacion_doctor(self):
        with self.app.app_context():
            doctor = Doctor(
                nombre="Dr. Juan López",
                cedula="1234567890",
                genero="Masculino",
                especialidad="Cardiología",
                telefono="0987654321",
                cargo="Cardiólogo"
            )
            db.session.add(doctor)
            db.session.commit()

            resultado = Doctor.query.filter_by(cedula="1234567890").first()
            self.assertIsNotNone(resultado)
            self.assertEqual(resultado.nombre, "Dr. Juan López")

if __name__ == '__main__':
    unittest.main()
