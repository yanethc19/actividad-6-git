import pytest

from calculadora import precio_final
from main import calcular_ticket, main


def test_ticket_coincide_con_precio_final():
    subtotal, iva, total = calcular_ticket(100, 10)
    assert (subtotal, iva) == (90, 14.4)
    assert total == precio_final(100, 10)


def test_ticket_sin_descuento():
    assert calcular_ticket(250) == (250, 40, 290)


def test_ticket_descuento_invalido():
    with pytest.raises(ValueError):
        calcular_ticket(100, 120)


def test_main_try(capsys):
    codigo = main(["100", "10"])
    salida = capsys.readouterr().out
    assert codigo == 0
    assert "Total:    $104.40" in salida


def test_main_exception(capsys):
    codigo = main(["-50", "10"])
    salida = capsys.readouterr().out
    assert codigo == 1
    assert "Error: El precio no puede ser negativo" in salida