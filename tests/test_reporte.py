import unittest
from app import create_app, db
from app.model.cajadiaria import CajaDiaria
from datetime import date, timedelta

class ReporteTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            
            hoy = date.today()
            ayer = hoy - timedelta(days=1)

            # Simulamos dos cajas
            caja1 = CajaDiaria(fecha=ayer, monto_total=100.0)
            caja2 = CajaDiaria(fecha=hoy, monto_total=200.0)
            db.session.add_all([caja1, caja2])
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_reporte_balance_general(self):
        """Prueba el balance total de las cajas generadas."""
        response = self.client.get('/reportes/')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIn('total_general', data)
        self.assertEqual(data['total_general'], 300.0)
        self.assertEqual(len(data['detalle_por_dia']), 2)

if __name__ == '__main__':
    unittest.main()
