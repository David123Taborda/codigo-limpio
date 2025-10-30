from src.model.Calculadora import (
    calcular_ingreso_total_anual,
    calcular_deducciones_por_ley,
    calcular_deducciones_personales,
    calcular_renta_exenta,
    calcular_base_gravable,
    ErrorValorNegativo,
    ErrorTipoDato,
)
from src.db_conection import insertar_resultado

class CalculadoraController:
    def __init__(self):
        pass

    def procesar_calculo(self, sueldo, otros_ingresos, aporte_pension,
                         credito_vivienda, gasto_medicina, personas_a_cargo, patrimonio):
        try:
            ingresos_totales = calcular_ingreso_total_anual(
                sueldo, otros_ingresos, personas_a_cargo, patrimonio
            )
            deducciones_ley = calcular_deducciones_por_ley(aporte_pension)
            deducciones_personales = calcular_deducciones_personales(
                credito_vivienda, gasto_medicina
            )
            renta_exenta = calcular_renta_exenta(ingresos_totales, deducciones_ley)
            base_gravable = calcular_base_gravable(
                ingresos_totales, deducciones_ley, deducciones_personales, renta_exenta
            )

            # Guarda el resultado en la base de datos
            insertar_resultado(ingresos_totales, deducciones_ley,
                               deducciones_personales, renta_exenta, base_gravable)

            return {
                "ingreso_total": ingresos_totales,
                "deducciones_ley": deducciones_ley,
                "deducciones_personales": deducciones_personales,
                "renta_exenta": renta_exenta,
                "base_gravable": base_gravable
            }

        except (ValueError, ErrorValorNegativo, ErrorTipoDato) as e:
            raise e

    def modificar_ultimo_resultado(self, nuevo_valor):
        from src.db_conection import obtener_historial, modificar_resultado
        historial = obtener_historial()
        if historial:
            id_ultimo = historial[-1][0]  # Asume que el primer campo es 'id'
            modificar_resultado(id_ultimo, nuevo_valor)
            return True
        return False

    from src.db_conection import obtener_historial

def obtener_historial_resultados(self):
    return self.obtener_historial()
