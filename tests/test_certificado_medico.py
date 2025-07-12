import unittest
import os
from app import create_app, db
from app.model.paciente import Paciente
from app.model.doctor import Doctor
from app.model.cita import Cita
from app.model.certificado_medico import CertificadoMedico
from datetime import datetime

class CertificadoMedicoTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

            self.paciente = Paciente(
                nombre='Paciente Prueba',
                cedula='1111111111',
                genero='Masculino',
                telefono='099999999',
                direccion='Calle falsa 123',
                historial_medico='Ninguno',
                fecha_nacimiento='1995-01-01'
            )
            self.doctor = Doctor(
                nombre='Doctor Prueba',
                cedula='2222222222',
                genero='Femenino',
                especialidad='General',
                telefono='0988888888',
                cargo='Titular'
            )

            db.session.add_all([self.paciente, self.doctor])
            db.session.commit()

            self.cita = Cita(
                fecha_hora=datetime.utcnow(),
                estado='completada',
                motivo='Chequeo',
                paciente_id=self.paciente.id,
                doctor_id=self.doctor.id
            )
            db.session.add(self.cita)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

        # Limpia archivos PDF si se generan
        pdf_path = f"pdf_certificados/certificado_1.pdf"
        if os.path.exists(pdf_path):
            os.remove(pdf_path)

    def test_crear_certificado(self):
        payload = {
            "tipo": "Reposo médico",
            "descripcion": "El paciente requiere reposo por 5 días.",
            "paciente_id": self.paciente.id,
            "doctor_id": self.doctor.id,
            "cita_id": self.cita.id
        }

        response = self.client.post('/certificados/', json=payload)
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn("id", data)
        self.assertEqual(data["message"], "Certificado creado")

        # Verifica que el PDF se haya generado
        pdf_path = f"pdf_certificados/certificado_{data['id']}.pdf"
        self.assertTrue(os.path.exists(pdf_path))

    def test_certificado_es_vigente(self):
        with self.app.app_context():
            certificado = CertificadoMedico(
                tipo="Deporte",
                descripcion="Apto para actividades deportivas.",
                fecha_emision=datetime.utcnow(),
                paciente_id=self.paciente.id,
                doctor_id=self.doctor.id,
                cita_id=self.cita.id
            )
            db.session.add(certificado)
            db.session.commit()
            self.assertTrue(certificado.es_vigente())

if __name__ == '__main__':
    unittest.main()
