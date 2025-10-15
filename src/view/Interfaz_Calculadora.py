import sys
sys.path.append("src")

from model.Calculadora import (
    calcular_ingreso_total_anual,
    calcular_deducciones_por_ley,
    calcular_deducciones_personales,
    calcular_renta_exenta,
    calcular_base_gravable,
    ErrorValorNegativo,
    ErrorTipoDato,
)


def main():
    try:
        sueldo_mensual = float(input("Ingresa tu sueldo mensual: "))
        otros_ingresos = float(input("Ingresa tus otros ingresos: "))
        aporte_pension = float(input("Ingresa tu aporte a pensión: "))
        credito_vivienda = float(input("Ingresa el valor de tu crédito de vivienda: "))
        gasto_medicina = float(input("Ingresa tus gastos en salud: "))
        numero_personas = int(input("Ingresa el número de personas a repartir los ingresos: "))
        patrimonio = float(input("Ingresa tu patrimonio: "))

        ingresos_totales = calcular_ingreso_total_anual(
            sueldo=sueldo_mensual,
            otros_ingresos=otros_ingresos,
            numero_personas=numero_personas,
            patrimonio=patrimonio,
        )

        deducciones_por_ley = calcular_deducciones_por_ley(aporte_pension)
        deducciones_personales = calcular_deducciones_personales(credito_vivienda, gasto_medicina)
        renta_exenta_calculada = calcular_renta_exenta(ingresos_totales, deducciones_por_ley)
        base_gravable = calcular_base_gravable(
            ingresos_totales,
            deducciones_por_ley,
            deducciones_personales,
            renta_exenta_calculada,
        )

        print(
            f"\n--- Resultados ---\n"
            f"Ingresos totales: {ingresos_totales}\n"
            f"Deducciones por ley: {deducciones_por_ley}\n"
            f"Deducciones personales: {deducciones_personales}\n"
            f"Renta exenta: {renta_exenta_calculada}\n"
            f"Base gravable: {base_gravable}\n"
        )

    except ErrorValorNegativo as e:
        print(f"Error: {e}")
    except ErrorTipoDato as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
