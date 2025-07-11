from unittest.mock import MagicMock

# Simulamos una clase similar a Paciente sin conexión a SQLAlchemy
class FakePaciente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

def test_mock_paciente():
    paciente_mock = MagicMock(spec=FakePaciente)
    paciente_mock.nombre = "Luis"
    paciente_mock.cedula = "0000000000"
    paciente_mock.guardar = MagicMock(return_value="Guardado")

    assert paciente_mock.nombre == "Luis"
    assert paciente_mock.guardar() == "Guardado"
    paciente_mock.guardar.assert_called_once()
