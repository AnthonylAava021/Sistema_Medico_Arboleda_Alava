from unittest.mock import MagicMock

# Creamos una clase simulada para evitar dependencias de SQLAlchemy
class FakeDoctor:
    def __init__(self, nombre, cedula, especialidad):
        self.nombre = nombre
        self.cedula = cedula
        self.especialidad = especialidad

def test_mock_doctor():
    doctor_mock = MagicMock(spec=FakeDoctor)
    doctor_mock.nombre = "Dr. Simulado"
    doctor_mock.cedula = "1112223334"
    doctor_mock.especialidad = "Neurología"
    doctor_mock.guardar = MagicMock(return_value="Guardado")

    assert doctor_mock.nombre == "Dr. Simulado"
    assert doctor_mock.guardar() == "Guardado"
    doctor_mock.guardar.assert_called_once()
