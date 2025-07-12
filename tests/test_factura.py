import unittest
from app import create_app, db
from app.model.paciente import Paciente
from app.model.doctor import Doctor
from app.model.cita import Cita
from app.model.factura import Factura
from datetime import datetime

class FacturaTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

            # Crear paciente
            self.paciente = Paciente(
                nombre='Paciente Factura',
                cedula='1234567890',
                genero='Masculino',
                telefono='099999999',
                direccion='Av. Test',
                historial_medico='Sin antecedentes',
                fecha_nacimiento='1990-01-01'
            )
            # Crear doctor
            self.doctor = Doctor(
                nombre='Doctor Factura',
                cedula='0987654321',
                genero='Femenino',
                especialidad='Pediatría',
                telefono='099111222',
                cargo='Principal'
            )
            db.session.add_all([self.paciente, self.doctor])
            db.session.commit()

            # Crear cita
            self.cita = Cita(
                fecha_hora=datetime.utcnow(),
                estado='pendiente',
                motivo='Chequeo general',
                paciente_id=self.paciente.id,
                doctor_id=self.doctor.id
            )
            db.session.add(self.cita)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_crear_factura(self):
        """Verifica que se pueda crear una factura correctamente."""
        payload = {
            "cedula": self.paciente.cedula,
            "monto": 80.0,
            "metodo_pago": "Efectivo",
            "cita_id": self.cita.id
        }

        response = self.client.post('/facturas/', json=payload)
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn("id", data)
        self.assertEqual(data["message"], "Factura creada")

    def test_obtener_facturas(self):
        """Verifica que se obtenga la lista de facturas."""
        # Crear factura manualmente
        with self.app.app_context():
            factura = Factura(
                monto=100.0,
                metodo_pago="Tarjeta",
                estado="pagado",
                paciente_id=self.paciente.id,
                cita_id=self.cita.id
            )
            db.session.add(factura)
            db.session.commit()

        response = self.client.get('/facturas/')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 1)
        self.assertIn("paciente", data[0])
        self.assertIn(self.paciente.nombre, data[0]["paciente"])

if __name__ == '__main__':
    unittest.main()
