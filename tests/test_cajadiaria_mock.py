from unittest.mock import MagicMock
from datetime import date

class FakeCajaDiaria:
    fecha = None
    monto_total = None
    def guardar(self):
        return "Guardado"

def test_mock_caja_diaria():
    caja_mock = MagicMock(spec=FakeCajaDiaria)
    caja_mock.fecha = date(2025, 7, 12)
    caja_mock.monto_total = 1234.56
    caja_mock.guardar = MagicMock(return_value="Guardado")

    assert caja_mock.fecha == date(2025, 7, 12)
    assert caja_mock.monto_total == 1234.56
    assert caja_mock.guardar() == "Guardado"
    caja_mock.guardar.assert_called_once()
