import subprocess
import sys


def ejecutar(*argumentos):
    """Ejecuta main.py como lo haría un usuario desde la terminal."""
    return subprocess.run(
        [sys.executable, "main.py", *argumentos],
        capture_output=True,
        text=True,
    )


def test_sistema_try():
    resultado = ejecutar("100", "10")
    assert resultado.returncode == 0
    assert resultado.stdout.splitlines() == [
        "Subtotal: $90.00",
        "IVA:      $14.40",
        "Total:    $104.40",
    ]


def test_sistema_exception_descuento():
    resultado = ejecutar("100", "120")
    assert resultado.returncode == 1
    assert "Error: El descuento debe estar entre 0 y 100" in resultado.stdout


def test_sistema_exception_texto():
    resultado = ejecutar("abc")
    assert resultado.returncode == 1
    assert "Error:" in resultado.stdout


def test_sistema_exception_sin_precio():
    resultado = ejecutar()
    assert resultado.returncode == 1
    assert "falta el precio" in resultado.stdout