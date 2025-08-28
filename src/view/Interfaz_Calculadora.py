import sys
sys.path.append("src")
from model.Calculadora import calcular_ingresos_total_anuales, calcular_deducciones_por_ley, deducciones_personales, renta_exenta, calcular_base_del_impuesto, ErrorValorNegativo, ErrorTipoDato

import unittest


try:

    sueldo_mensual = float(input("Ingresa  tu sueldo mensual."))
    otros_ingresos = float(input("Ingresa tus otros ingresos."))
    aporte_pension = float(input("Ingresa tu aporte a pensión."))
    credito_vivienda = float(input("Ingresa el valor de tu crédito de vivienda."))
    gasto_medicina = float(input("Ingresa tu aporte a salud."))
    numero_personas = int(input("Ingresa el número de personas a repartir los ingresos."))
    patrimonio = float(input("Ingresa tu patrimonio."))
    gastos_normales = float(input("Ingresa tus gastos normales."))
    consignaciones = float(input("Ingresa tus consignaciones."))

    ingresos_totales = calcular_ingresos_total_anuales(sueldo_mensual, otros_ingresos, numero_personas, patrimonio)

    deducciones_por_ley = calcular_deducciones_por_ley(aporte_pension)
    deducciones_personales = deducciones_personales(credito_vivienda, gasto_medicina)
    renta_exenta = renta_exenta(ingresos_totales, deducciones_por_ley)
    calcular_base_del_impuesto = calcular_base_del_impuesto(ingresos_totales, deducciones_por_ley, deducciones_personales, renta_exenta)

    print(f"Las salidas esperadas de acuerdo a los datos pedidos son: n/ Ingresos totales: {ingresos_totales} n/ Deducciones por ley: {deducciones_por_ley} n/ Deducciones personales: {deducciones_personales} n/ Renta exenta: {renta_exenta} n/ Base sobre la que se paga impuesto: {base_sobre_la_que_se_paga_impuesto}")

except ErrorValorNegativo as e:
    print(f"Error: {e}")

except ErrorTipoDato as e:
    print(f"Error: {e}")


