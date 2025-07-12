import unittest
from datetime import date
from flask import Flask
from app.configuracion_base import db
from app.model.cajadiaria import CajaDiaria

class TestCajaDiariaModel(unittest.TestCase):
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

    def test_crear_caja_diaria(self):
        with self.app.app_context():
            caja = CajaDiaria(fecha=date.today(), monto_total=2000.00)
            db.session.add(caja)
            db.session.commit()

            resultado = CajaDiaria.query.filter_by(fecha=date.today()).first()
            self.assertIsNotNone(resultado)
            self.assertEqual(resultado.monto_total, 2000.00)

if __name__ == '__main__':
    unittest.main()
