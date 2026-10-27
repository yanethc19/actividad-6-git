import sys

from calculadora import calcular_iva, precio_con_descuento


def calcular_ticket(precio, descuento=0):
    """Regresa el subtotal, el IVA y el total usando las funciones de calculadora."""
    subtotal = precio_con_descuento(precio, descuento)
    iva = calcular_iva(subtotal)
    return subtotal, iva, round(subtotal + iva, 2)


def main(argumentos):
    """Lee el precio y el descuento, imprime el ticket y regresa el código de salida."""
    try:
        precio = float(argumentos[0])
        descuento = float(argumentos[1]) if len(argumentos) > 1 else 0
        subtotal, iva, total = calcular_ticket(precio, descuento)
    except IndexError:
        print("Error: falta el precio. Uso: python main.py <precio> [descuento]")
        return 1
    except ValueError as error:
        print(f"Error: {error}")
        return 1

    print(f"Subtotal: ${subtotal:.2f}")
    print(f"IVA:      ${iva:.2f}")
    print(f"Total:    ${total:.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))