import unittest
from Calculadora import calcular_ingresos_total_anuales

class PruebasCalculadora(unittest.TestCase):

    # Caso normal 1
    def test_normal_1(self):
        sueldo = 2000000
        otros_ingresos = 500000
        esperado = 2500000 * 12
        self.assertEqual(calcular_ingresos_total_anuales(sueldo, otros_ingresos), esperado)

    # Caso normal 2
    def test_normal_2(self):
        sueldo = 1000000
        otros_ingresos = 1000000
        esperado = 2000000 * 12
        self.assertEqual(calcular_ingresos_total_anuales(sueldo, otros_ingresos), esperado)

    # Caso normal 3
    def test_normal_3(self):
        sueldo = 1500000
        otros_ingresos = 0
        esperado = 1500000 * 12
        self.assertEqual(calcular_ingresos_total_anuales(sueldo, otros_ingresos), esperado)

    # Caso extraordinario 1
    def test_extraordinario_1(self):
        sueldo = 5000000
        otros_ingresos = 2000000
        esperado = 7000000 * 12
        self.assertEqual(calcular_ingresos_total_anuales(sueldo, otros_ingresos), esperado)

    # Caso extraordinario 2
    def test_extraordinario_2(self):
        sueldo = 10000000
        otros_ingresos = 0
        esperado = 126000000
        self.assertEqual(calcular_ingresos_total_anuales(sueldo, otros_ingresos), esperado)

    # Caso de error
    def test_error_sueldo_negativo(self):
        sueldo = -1000
        otros_ingresos = 500
        with self.assertRaises(ValueError):
            calcular_ingresos_total_anuales(sueldo, otros_ingresos)


if __name__ == '__main__':
    unittest.main()
