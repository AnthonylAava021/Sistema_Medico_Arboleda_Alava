import unittest
from app import create_app, db
from app.model.paciente import Paciente
from flask import json

class PacienteTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        self.paciente_data = {
            "nombre": "Juan Pérez",
            "cedula": "1234567890",
            "telefono": "0999999999",
            "genero": "Masculino",
            "direccion": "Quito",
            "historial_medico": "Ninguno",
            "fecha_nacimiento": "1990-01-01"
        }

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_crear_paciente(self):
        response = self.client.post(
            "/pacientes/",
            data=json.dumps(self.paciente_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data["nombre"], "Juan Pérez")
        self.assertEqual(data["cedula"], "1234567890")

    def test_listar_pacientes(self):
        # Primero se crea uno
        self.client.post(
            "/pacientes/",
            data=json.dumps(self.paciente_data),
            content_type='application/json'
        )
        # Luego se lista
        response = self.client.get("/pacientes/")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["nombre"], "Juan Pérez")

if __name__ == '__main__':
    unittest.main()
