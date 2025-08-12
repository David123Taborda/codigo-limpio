import unittest
from Calculadora import calcular_ingresos_total_anuales

class PruebasCalculadora(unittest.TestCase):

    def test_calcular_ingresos_total_anuales(self):
        sueldo = 4500000
        otros_ingresos = 6000000

        # Llamamos a la función para calcular los ingresos totales anuales
        ingresos_totales = calcular_ingresos_total_anuales(sueldo, otros_ingresos)

        # Comprobamos que los ingresos totales anuales son correctos
        ingresos_esperados = 60000000
        self.assertAlmostEqual(ingresos_totales, ingresos_esperados, 0)


    def test_extraordinario_1(self):
        sueldo = 0
        otros_ingresos = 120000000

        # Llamamos a la función para calcular los ingresos totales anuales
        ingresos_totales = calcular_ingresos_total_anuales(sueldo, otros_ingresos)

        # Comprobamos que los ingresos totales anuales son correctos
        ingresos_esperados = 120000000
        self.assertAlmostEqual(ingresos_totales, ingresos_esperados, 0)

    def test_extraordinario_2(self):
        sueldo = 10000000
        otros_ingresos = 0

        # Llamamos a la función para calcular los ingresos totales anuales
        ingresos_totales = calcular_ingresos_total_anuales(sueldo, otros_ingresos)

        # Comprobamos que los ingresos totales anuales son correctos
        ingresos_esperados = 126000000
        self.assertAlmostEqual(ingresos_totales, ingresos_esperados, 2)

    def test_extraordinario_3(self):
        sueldo = 2500000
        otros_ingresos = 30000000

        # Llamamos a la función para calcular los ingresos totales anuales
        ingresos_totales = calcular_ingresos_total_anuales(sueldo, otros_ingresos)

        # Comprobamos que los ingresos totales anuales son correctos
        ingresos_esperados = 36000000
        self.assertAlmostEqual(ingresos_totales, ingresos_esperados, 2)



if __name__ == '__main__':
    unittest.main()
