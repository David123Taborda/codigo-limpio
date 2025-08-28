import unittest
import sys
sys.path.append("src")

from src.model.Calculadora import calcular_ingresos_total_anuales, ErrorValorNegativo, ErrorTipoDato

class PruebasCalculadora(unittest.TestCase):

    # Caso normal 1
        def test_normal_1(self):
        sueldo = 4500000
        otros_ingresos = 500000
        esperado = (4500000 * 12 + 6000000)  # Sueldo mensual + otros ingresos + 6000000
        self.assertEqual(calcular_ingresos_total_anuales(sueldo, otros_ingresos), esperado)

    # Caso normal 2
    def test_normal_2(self):
        sueldo = 1000000
        otros_ingresos = 1000000
        esperado = 1000000 * 12 + 6000000  # Sueldo mensual + otros ingresos + 6000000
        self.assertEqual(calcular_ingresos_total_anuales(sueldo, otros_ingresos), esperado)

    # Caso normal 3
    def test_normal_3(self):
        sueldo = 1500000
        otros_ingresos = 0
        esperado = 1500000 * 12 + 6000000  # Sueldo mensual + otros ingresos + 6000000
        self.assertEqual(calcular_ingresos_total_anuales(sueldo, otros_ingresos), esperado)

    # Caso extraordinario 1
    def test_extraordinario_1(self):
        sueldo = 5000000
        otros_ingresos = 2000000
        esperado = 5000000 * 12 + 6000000  # Sueldo mensual + otros ingresos + 6000000
        self.assertEqual(calcular_ingresos_total_anuales(sueldo, otros_ingresos), esperado)

    # Caso extraordinario 2
    def test_extraordinario_2(self):
        sueldo = 10000000
        otros_ingresos = 0
        esperado = 10000000 * 12 + 6000000  # Sueldo mensual + otros ingresos + 6000000
        self.assertEqual(calcular_ingresos_total_anuales(sueldo, otros_ingresos), esperado)


    def test_extraordinario_3(self):
        sueldo = 3000000
        otros_ingresos = 1000000 
        esperado =  3000000 * 12 + 6000000  # Sueldo mensual + otros ingresos + 6000000 
        self.assertEqual(calcular_ingresos_total_anuales(sueldo, otros_ingresos), esperado) 

    # Caso de error
    def test_error_sueldo_negativo(self):
        sueldo = -3000000
        otros_ingresos = 0
        with self.assertRaises(ErrorValorNegativo):
            calcular_ingresos_total_anuales(sueldo, otros_ingresos)

    def test_error_otros_ingresos_negativos(self):
        sueldo = 3000000
        otros_ingresos = -2000000
        with self.assertRaises(ErrorValorNegativo):
            calcular_ingresos_total_anuales(sueldo, otros_ingresos)

    def test_error_numero_personas_negativo(self):
        sueldo = 4000000
        otros_ingresos = 1000000
        numero_personas = -1
        with self.assertRaises(ErrorValorNegativo):
            calcular_ingresos_total_anuales(sueldo, otros_ingresos, numero_personas)                

    def test_error_tipo_otros_ingresos(self):
        sueldo = 3000000
        otros_ingresos = 1000000
        numero_personas = 0
        patrimonio = -1000000
        with self.assertRaises(ErrorValorNegativo):
            calcular_ingresos_total_anuales(sueldo, otros_ingresos, numero_personas, patrimonio)
    
if __name__ == '__main__':
    unittest.main()
