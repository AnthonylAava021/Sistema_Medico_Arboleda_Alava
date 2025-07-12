import unittest
from app import create_app, db
from app.model.paciente import Paciente
from app.model.doctor import Doctor
from app.model.cita import Cita
from app.model.factura import Factura
from datetime import datetime, timedelta

class CajaDiariaTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

            self.paciente = Paciente(
                nombre='Paciente Caja',
                cedula='1234567891',
                genero='Femenino',
                telefono='0991234567',
                direccion='Test Dir',
                historial_medico='Sin antecedentes',
                fecha_nacimiento='1995-06-15'
            )
            self.doctor = Doctor(
                nombre='Doctor Caja',
                cedula='1098765432',
                genero='Masculino',
                especialidad='General',
                telefono='098111222',
                cargo='Titular'
            )
            db.session.add_all([self.paciente, self.doctor])
            db.session.commit()

            self.cita = Cita(
                fecha_hora=datetime.utcnow(),
                estado='pendiente',
                motivo='Chequeo',
                paciente_id=self.paciente.id,
                doctor_id=self.doctor.id
            )
            db.session.add(self.cita)
            db.session.commit()

            # Crear factura para hoy
            factura = Factura(
                monto=150.0,
                estado='pagado',
                metodo_pago='Efectivo',
                paciente_id=self.paciente.id,
                cita_id=self.cita.id,
                fecha=datetime.utcnow()  # importante para que entre en el cálculo diario
            )
            db.session.add(factura)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_generar_caja_diaria(self):
        """Prueba la generación de la caja diaria para la fecha actual."""
        fecha_str = datetime.utcnow().strftime("%Y-%m-%d")
        response = self.client.post('/caja/', json={'fecha': fecha_str})
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['fecha'], fecha_str)
        self.assertEqual(data['monto_total'], 150.0)

    def test_obtener_cajas(self):
        """Prueba que se puedan recuperar las cajas diarias."""
        # Primero generamos una caja
        fecha_str = datetime.utcnow().strftime("%Y-%m-%d")
        self.client.post('/caja/', json={'fecha': fecha_str})

        # Ahora verificamos el GET
        response = self.client.get('/caja/')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(isinstance(data, list))
        self.assertGreaterEqual(len(data), 1)
        self.assertEqual(data[0]['monto_total'], 150.0)

if __name__ == '__main__':
    unittest.main()
