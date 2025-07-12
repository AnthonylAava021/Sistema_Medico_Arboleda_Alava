import unittest
from app import create_app, db
from app.model.usuario import Usuario, UserRole

class UsuarioTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def registrar_usuario(self, username, email, password, role='paciente'):
        return self.client.post('/usuarios/register', json={
            'username': username,
            'email': email,
            'password': password,
            'role': role
        })

    def test_registro_exitoso(self):
        res = self.registrar_usuario('juan', 'juan@mail.com', '1234')
        self.assertEqual(res.status_code, 201)
        self.assertIn('juan', res.get_data(as_text=True))

    def test_registro_duplicado(self):
        self.registrar_usuario('ana', 'ana@mail.com', '1234')
        res = self.registrar_usuario('ana', 'ana@mail.com', '1234')
        self.assertEqual(res.status_code, 400)
        self.assertIn('ya registrado', res.get_data(as_text=True))

    def test_login_exitoso(self):
        self.registrar_usuario('luis', 'luis@mail.com', '1234')
        res = self.client.post('/usuarios/login', json={
            'username': 'luis',
            'password': '1234'
        })
        self.assertEqual(res.status_code, 200)
        self.assertIn('access_token', res.get_json())

    def test_login_invalido(self):
        res = self.client.post('/usuarios/login', json={
            'username': 'nadie',
            'password': 'fake'
        })
        self.assertEqual(res.status_code, 401)
