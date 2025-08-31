


class ErrorValorNegativo(Exception):
    """Excepción personalizada para valores negativos."""

class ErrorTipoDato(Exception):
    """Excepción personalizada para tipos de datos incorrectos."""


def calcular_ingresos_total_anuales(sueldo: int|float, otros_ingresos: int|float, numero_personas: int =1, patrimonio: int =0):
    if not isinstance(sueldo, (int, float)):
        raise ErrorTipoDato("El sueldo debe ser numérico")
    if not isinstance(otros_ingresos, (int, float)):
        raise ErrorTipoDato("Los otros ingresos deben ser numéricos")
    if sueldo < 0:
        raise ErrorValorNegativo("El sueldo no puede ser negativo")
    if otros_ingresos < 0:
        raise ErrorValorNegativo("Los otros ingresos no puede ser negativo") 
    if numero_personas < 0:
        raise ErrorValorNegativo("El número de personas no puede ser negativo")
    if patrimonio < 0:
        raise ErrorValorNegativo("El patrimonio no puede ser negativo")

    return (sueldo * 12) + 6000000


def calcular_deducciones_por_ley(aporte_pension: float):    
    return aporte_pension + 3000000

def calcular_deducciones_personales(credito_vivienda: float, gasto_medicina: float):
    return credito_vivienda + gasto_medicina

def renta_exenta(ingresos_totales: float, deducciones_por_ley: float):
    return 0.25 * (ingresos_totales - deducciones_por_ley)

def base_sobre_la_que_se_paga_impuesto(ingresos_totales: float, deducciones_por_ley: float, calcular_deducciones_personales: float, renta_exenta: float):
    return ingresos_totales - deducciones_por_ley - calcular_deducciones_personales - renta_exenta

