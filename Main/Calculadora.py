def calcular_ingresos_total_anuales(sueldo, otros_ingresos, numero_personas=1, patrimonio=0):
    if not isinstance(sueldo, (int, float)):
        raise TypeError("El sueldo debe ser numérico")
    if not isinstance(otros_ingresos, (int, float)):
        raise TypeError("Los otros ingresos deben ser numéricos")
    if sueldo < 0:
        raise ValueError("El sueldo no puede ser negativo")
    if otros_ingresos < 0:
        raise ValueError("Los otros ingresos no pueden ser negativos")
    if numero_personas < 0:
        raise ValueError("El número de personas no puede ser negativo")
    if patrimonio < 0:
        raise ValueError("El patrimonio no puede ser negativo")
    
    return (sueldo * 12) + 6000000


def calcular_deducciones_por_ley(aporte_pension):    
    return aporte_pension + 3000000

def deducciones_personales(credito_vivienda, gasto_medicina):
    return credito_vivienda + gasto_medicina

def renta_exenta(ingresos_totales, deducciones_por_ley):
    return 0.25 * (ingresos_totales - deducciones_por_ley)

def base_sobre_la_que_se_paga_impuesto(ingresos_totales, deducciones_por_ley, deducciones_personales, renta_exenta):
    return ingresos_totales - deducciones_por_ley - deducciones_personales - renta_exenta

