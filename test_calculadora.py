def precio_con_descuento(precio, descuento):
    """Regresa el precio después de aplicar un descuento en porcentaje."""
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    if descuento < 0 or descuento > 100:
        raise ValueError("El descuento debe estar entre 0 y 100")
    return round(precio - precio * descuento / 100, 2)


def calcular_iva(precio, tasa=16):
    """Regresa el IVA de un precio (por defecto 16 %)."""
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    return round(precio * tasa / 100, 2)


def precio_final(precio, descuento=0, tasa=16):
    """Aplica el descuento y después le suma el IVA."""
    subtotal = precio_con_descuento(precio, descuento)
    return round(subtotal + calcular_iva(subtotal, tasa), 2)