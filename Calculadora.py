def calcular_ingresos_total_anuales(sueldo_mensual, otros_ingresos):
    """Calcula el total de los ingresos anuales."""
    ingresos_anuales = (sueldo_mensual * 12) + otros_ingresos
    return ingresos_anuales

def prueba_normal_1():
    sueldo = 45000000
    otros_ingresos = 12000000
    ingresos_totales = calcular_ingresos_total_anuales(sueldo, otros_ingresos)

    ingresos_esperados = 60000000

    if round(ingresos_totales, 2) == round(ingresos_esperados, 2):
        print("Prueba normal 1: Éxito")
    else:
        print("Prueba normal 1: Fallo")

prueba_normal_1()
