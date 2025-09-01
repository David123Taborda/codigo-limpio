class ErrorValorNegativo(Exception):
    """Excepción personalizada para valores negativos."""


class ErrorTipoDato(Exception):
    """Excepción personalizada para tipos de datos incorrectos."""


# Constantes para evitar números mágicos
AUXILIO_TRANSPORTE_ANUAL = 6_000_000
DEDUCCION_LEY_FIJA = 3_000_000
PORCENTAJE_RENTA_EXENTA = 0.25


def calcular_ingreso_total_anual(
    sueldo: int | float, 
    otros_ingresos: int | float, 
    numero_personas: int = 1, 
    patrimonio: int = 0
) -> float:
    """
    Calcula el ingreso total anual a partir del sueldo mensual, 
    otros ingresos, número de personas y patrimonio.
    """
    if not isinstance(sueldo, (int, float)):
        raise ErrorTipoDato("El sueldo debe ser numérico")
    if not isinstance(otros_ingresos, (int, float)):
        raise ErrorTipoDato("Los otros ingresos deben ser numéricos")
    if sueldo < 0:
        raise ErrorValorNegativo("El sueldo no puede ser negativo")
    if otros_ingresos < 0:
        raise ErrorValorNegativo("Los otros ingresos no pueden ser negativos") 
    if numero_personas < 0:
        raise ErrorValorNegativo("El número de personas no puede ser negativo")
    if patrimonio < 0:
        raise ErrorValorNegativo("El patrimonio no puede ser negativo")

    return (sueldo * 12) + AUXILIO_TRANSPORTE_ANUAL + otros_ingresos


def calcular_deducciones_por_ley(aporte_pension: float) -> float:
    """
    Calcula las deducciones de ley sumando el aporte a pensión y
    la deducción fija establecida por la norma.
    """
    return aporte_pension + DEDUCCION_LEY_FIJA


def calcular_deducciones_personales(credito_vivienda: float, gasto_medicina: float) -> float:
    """
    Calcula las deducciones personales por crédito de vivienda y gastos médicos.
    """
    return credito_vivienda + gasto_medicina


def calcular_renta_exenta(ingresos_totales: float, deducciones_por_ley: float) -> float:
    """
    Calcula la renta exenta como el 25% de los ingresos netos después de 
    aplicar deducciones de ley.
    """
    return PORCENTAJE_RENTA_EXENTA * (ingresos_totales - deducciones_por_ley)


def calcular_base_gravable(
    ingresos_totales: float, 
    deducciones_por_ley: float, 
    deducciones_personales: float, 
    renta_exenta: float
) -> float:
    """
    Calcula la base gravable sobre la que se pagará impuesto.
    """
    return ingresos_totales - deducciones_por_ley - deducciones_personales - renta_exenta
