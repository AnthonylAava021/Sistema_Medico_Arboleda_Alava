import unittest
from app import create_app, db
from app.model.paciente import Paciente
from app.model.doctor import Doctor
from app.model.cita import Cita
import json
from datetime import datetime

class CitaTestCase(unittest.TestCase):
    def setUp(self):
        # Configurar app para pruebas
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            # Crear paciente de prueba
            paciente = Paciente(
                nombre='Paciente Test',
                cedula='1234567890',
                genero='Masculino',
                telefono='0999999999',
                direccion='Calle Falsa 123',
                historial_medico='Ninguno',
                fecha_nacimiento='1990-01-01'
            )
            db.session.add(paciente)
            # Crear doctor de prueba
            doctor = Doctor(
                nombre='Doctor Test',
                cedula='0987654321',
                genero='Femenino',
                especialidad='Cardiología',
                telefono='0888888888',
                cargo='Especialista'
            )
            db.session.add(doctor)
            db.session.commit()
            self.paciente_id = paciente.id
            self.doctor_id = doctor.id

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_crear_cita(self):
        with self.app.app_context():
            data = {
                "fecha_hora": "2025-07-02T15:00:00",
                "estado": "pendiente",
                "motivo": "Consulta general",
                "paciente_id": self.paciente_id,
                "doctor_id": self.doctor_id
            }
            response = self.client.post('/citas/', json=data)
            self.assertEqual(response.status_code, 201)
            response_json = response.get_json()
            self.assertEqual(response_json['fecha_hora'], data['fecha_hora'])
            self.assertEqual(response_json['estado'], data['estado'])
            self.assertEqual(response_json['motivo'], data['motivo'])
            self.assertEqual(response_json['paciente_id'], data['paciente_id'])
            self.assertEqual(response_json['doctor_id'], data['doctor_id'])

    def test_listar_citas(self):
        with self.app.app_context():
            # Crear una cita directamente para probar listado
            cita = Cita(
                fecha_hora=datetime.fromisoformat("2025-07-02T15:00:00"),
                estado='pendiente',
                motivo='Consulta general',
                paciente_id=self.paciente_id,
                doctor_id=self.doctor_id
            )
            db.session.add(cita)
            db.session.commit()

            response = self.client.get('/citas/')
            self.assertEqual(response.status_code, 200)
            citas = response.get_json()
            self.assertIsInstance(citas, list)
            self.assertGreaterEqual(len(citas), 1)
            self.assertEqual(citas[0]['motivo'], 'Consulta general')

if __name__ == '__main__':
    unittest.main()
