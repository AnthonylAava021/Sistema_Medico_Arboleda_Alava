import unittest
from app import create_app, db
from app.model.doctor import Doctor
from flask import json

class DoctorTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        self.doctor_data = {
            "nombre": "Dra. María Pérez",
            "cedula": "0912345678",
            "genero": "Femenino",
            "especialidad": "Pediatría",
            "telefono": "0987654321",
            "cargo": "Jefa de pediatría"
        }

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_crear_doctor(self):
        response = self.client.post(
            "/doctores/",
            data=json.dumps(self.doctor_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data["nombre"], "Dra. María Pérez")
        self.assertEqual(data["cedula"], "0912345678")

    def test_listar_doctores(self):
        # Crear doctor
        self.client.post(
            "/doctores/",
            data=json.dumps(self.doctor_data),
            content_type='application/json'
        )
        # Listar doctores
        response = self.client.get("/doctores/")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["nombre"], "Dra. María Pérez")

if __name__ == '__main__':
    unittest.main()
