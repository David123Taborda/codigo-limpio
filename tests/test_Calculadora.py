import unittest
import sys

sys.path.append("src")

from src.model.Calculadora import (
    calcular_ingreso_total_anual,
    ErrorValorNegativo,
    ErrorTipoDato,
)


class PruebasCalculadora(unittest.TestCase):
    BONO_ANUAL = 6_000_000
    MESES_DE_ANUALIDAD = 12

    # Casos normales
    def test_normal_1(self):
        sueldo = 4_500_000
        otros_ingresos = 500_000
        esperado = (sueldo * self.MESES_DE_ANUALIDAD) + self.BONO_ANUAL + otros_ingresos
        self.assertEqual(calcular_ingreso_total_anual(sueldo, otros_ingresos), esperado)

    def test_normal_2(self):
        sueldo = 1_000_000
        otros_ingresos = 1_000_000
        esperado = (sueldo * self.MESES_DE_ANUALIDAD) + self.BONO_ANUAL + otros_ingresos
        self.assertEqual(calcular_ingreso_total_anual(sueldo, otros_ingresos), esperado)

    def test_normal_3(self):
        sueldo = 1_500_000
        otros_ingresos = 0
        esperado = (sueldo * self.MESES_DE_ANUALIDAD) + self.BONO_ANUAL + otros_ingresos
        self.assertEqual(calcular_ingreso_total_anual(sueldo, otros_ingresos), esperado)

    # Casos extraordinarios
    def test_extraordinario_1(self):
        sueldo = 5_000_000
        otros_ingresos = 2_000_000
        esperado = (sueldo * self.MESES_DE_ANUALIDAD) + self.BONO_ANUAL + otros_ingresos
        self.assertEqual(calcular_ingreso_total_anual(sueldo, otros_ingresos), esperado)

    def test_extraordinario_2(self):
        sueldo = 10_000_000
        otros_ingresos = 0
        esperado = (sueldo * self.MESES_DE_ANUALIDAD) + self.BONO_ANUAL + otros_ingresos
        self.assertEqual(calcular_ingreso_total_anual(sueldo, otros_ingresos), esperado)

    def test_extraordinario_3(self):
        sueldo = 3_000_000
        otros_ingresos = 1_000_000
        esperado = (sueldo * self.MESES_DE_ANUALIDAD) + self.BONO_ANUAL + otros_ingresos
        self.assertEqual(calcular_ingreso_total_anual(sueldo, otros_ingresos), esperado)

    # Casos de error
    def test_error_sueldo_negativo(self):
        sueldo = -3_000_000
        otros_ingresos = 0
        with self.assertRaises(ErrorValorNegativo):
            calcular_ingreso_total_anual(sueldo, otros_ingresos)

    def test_error_otros_ingresos_negativos(self):
        sueldo = 3_000_000
        otros_ingresos = -2_000_000
        with self.assertRaises(ErrorValorNegativo):
            calcular_ingreso_total_anual(sueldo, otros_ingresos)

    def test_error_numero_personas_negativo(self):
        sueldo = 4_000_000
        otros_ingresos = 1_000_000
        numero_personas = -1
        with self.assertRaises(ErrorValorNegativo):
            calcular_ingreso_total_anual(sueldo, otros_ingresos, numero_personas)

    def test_error_patrimonio_negativo(self):
        sueldo = 3_000_000
        otros_ingresos = 1_000_000
        numero_personas = 0
        patrimonio = -1_000_000
        with self.assertRaises(ErrorValorNegativo):
            calcular_ingreso_total_anual(sueldo, otros_ingresos, numero_personas, patrimonio)


if __name__ == "__main__":
    unittest.main()
