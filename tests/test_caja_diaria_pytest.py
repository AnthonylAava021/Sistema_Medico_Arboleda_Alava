import pytest
from datetime import date
from flask import Flask
from app.configuracion_base import db
from app.model.cajadiaria import CajaDiaria

@pytest.fixture(scope='module')
def app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True
    db.init_app(app)

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture(scope='function')
def session(app):
    with app.app_context():
        yield db.session
        db.session.rollback()

def test_crear_caja_diaria(session):
    caja = CajaDiaria(fecha=date.today(), monto_total=1500.75)
    session.add(caja)
    session.commit()

    resultado = CajaDiaria.query.filter_by(fecha=date.today()).first()
    assert resultado is not None
    assert resultado.monto_total == 1500.75
