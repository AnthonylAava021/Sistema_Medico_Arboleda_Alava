import unittest
from app import create_app, db
from app.model.paciente import Paciente
from app.model.doctor import Doctor
from app.model.consulta import Consulta
from app.model.receta import Receta
from datetime import datetime

class RecetaTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

            self.paciente = Paciente(
                nombre='Paciente Test',
                cedula='1234567890',
                genero='Masculino',
                telefono='0999999999',
                direccion='Calle Falsa 123',
                historial_medico='Ninguno',
                fecha_nacimiento='1990-01-01'
            )
            self.doctor = Doctor(
                nombre='Doctor Test',
                cedula='0987654321',
                genero='Femenino',
                especialidad='Pediatría',
                telefono='0888888888',
                cargo='Titular'
            )
            db.session.add_all([self.paciente, self.doctor])
            db.session.commit()

            self.consulta = Consulta(
                diagnostico="Dolor de cabeza",
                notas="Tomar mucha agua",
                fecha=datetime.now(),
                paciente_id=self.paciente.id,
                doctor_id=self.doctor.id
            )
            db.session.add(self.consulta)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_crear_receta(self):
        data = {
            'medicamento': 'Paracetamol',
            'dosis': '500mg',
            'instrucciones': 'Cada 8 horas',
            'consulta_id': self.consulta.id
        }

        response = self.client.post('/recetas/', json=data)
        self.assertEqual(response.status_code, 201)
        receta = response.get_json()
        self.assertEqual(receta['medicamento'], 'Paracetamol')
        self.assertEqual(receta['dosis'], '500mg')
        self.assertEqual(receta['instrucciones'], 'Cada 8 horas')
        self.assertEqual(receta['consulta_id'], self.consulta.id)

    def test_obtener_receta_por_consulta(self):
        # Crear una receta manualmente en la BD
        with self.app.app_context():
            receta = Receta(
                medicamento='Amoxicilina',
                dosis='250mg',
                instrucciones='Cada 12 horas por 5 días',
                consulta_id=self.consulta.id
            )
            db.session.add(receta)
            db.session.commit()

        response = self.client.get(f'/recetas/consulta/{self.consulta.id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['medicamento'], 'Amoxicilina')
        self.assertEqual(data['consulta_id'], self.consulta.id)

if __name__ == '__main__':
    unittest.main()
