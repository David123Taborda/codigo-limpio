from Calculadora import calcular_ingresos_total_anuales


sueldo_mensual = float(input("Ingresa  tu sueldo mensual."))
otros_ingresos = float(input("Ingresa tus otros ingresos."))

ingresos_totales = calcular_ingresos_total_anuales(sueldo_mensual, otros_ingresos)



print(ingresos_totales)