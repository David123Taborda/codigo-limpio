def calcular_ingresos_total_anuales(sueldo, otros_ingresos):
    if not isinstance(sueldo, (int, float)):
        raise TypeError("El sueldo debe ser numérico")
    if not isinstance(otros_ingresos, (int, float)):
        raise TypeError("Los otros ingresos deben ser numéricos")
    if sueldo < 0:
        raise ValueError("El sueldo no puede ser negativo")
    if otros_ingresos < 0:
        raise ValueError("Los otros ingresos no pueden ser negativos")
    return (sueldo + otros_ingresos) * 12








