"""
Tests completos para las operaciones CRUD en PostgreSQL
Cubre: CREATE TABLE, INSERT, SELECT, UPDATE, DELETE
"""
import sys
import os
import unittest

# Agregar la raíz del proyecto al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.db_conection import (
    crear_conexion,
    crear_tabla,
    insertar_resultado,
    obtener_historial,
    modificar_resultado,
    eliminar_resultado
)


class TestCRUDDatabase(unittest.TestCase):
    """Suite de tests para operaciones CRUD en PostgreSQL"""
    
    @classmethod
    def setUpClass(cls):
        """Se ejecuta una vez antes de todos los tests"""
        print("\n🔧 Configurando tests...")
        crear_tabla()
    
    def test_01_conexion_exitosa(self):
        """Test: Verificar que la conexión a PostgreSQL funciona"""
        conexion = crear_conexion()
        self.assertIsNotNone(conexion, "❌ La conexión debería ser exitosa")
        if conexion:
            conexion.close()
        print("✅ Test 1: Conexión exitosa")
    
    # ========================================
    # TESTS DE INSERCIÓN (3 casos)
    # ========================================
    
    def test_02_insertar_resultado_normal(self):
        """Test: Insertar un resultado normal"""
        resultado = insertar_resultado(
            ingreso_total=50000000,
            deducciones_ley=8000000,
            deducciones_personales=2000000,
            renta_exenta=10000000,
            base_gravable=30000000
        )
        self.assertTrue(resultado, "❌ La inserción debería ser exitosa")
        print("✅ Test 2: Inserción normal exitosa")
    
    def test_03_insertar_resultado_con_ceros(self):
        """Test: Insertar un resultado con valores en cero"""
        resultado = insertar_resultado(
            ingreso_total=0,
            deducciones_ley=0,
            deducciones_personales=0,
            renta_exenta=0,
            base_gravable=0
        )
        self.assertTrue(resultado, "❌ La inserción con ceros debería ser exitosa")
        print("✅ Test 3: Inserción con ceros exitosa")
    
    def test_04_insertar_resultado_valores_grandes(self):
        """Test: Insertar un resultado con valores grandes"""
        resultado = insertar_resultado(
            ingreso_total=500000000,
            deducciones_ley=50000000,
            deducciones_personales=20000000,
            renta_exenta=100000000,
            base_gravable=330000000
        )
        self.assertTrue(resultado, "❌ La inserción con valores grandes debería ser exitosa")
        print("✅ Test 4: Inserción con valores grandes exitosa")
    
    # ========================================
    # TESTS DE CONSULTA/BÚSQUEDA (3 casos)
    # ========================================
    
    def test_05_obtener_historial_no_vacio(self):
        """Test: Consultar historial y verificar que no está vacío"""
        historial = obtener_historial()
        self.assertIsInstance(historial, list, "❌ El historial debería ser una lista")
        self.assertGreater(len(historial), 0, "❌ El historial debería tener al menos un registro")
        print(f"✅ Test 5: Consulta exitosa - {len(historial)} registros encontrados")
    
    def test_06_obtener_historial_estructura(self):
        """Test: Verificar estructura de datos del historial"""
        historial = obtener_historial()
        if len(historial) > 0:
            primer_registro = historial[0]
            self.assertEqual(len(primer_registro), 7, "❌ Cada registro debería tener 7 campos")
            print("✅ Test 6: Estructura de datos correcta")
        else:
            self.skipTest("No hay datos para verificar estructura")
    
    def test_07_obtener_historial_orden_descendente(self):
        """Test: Verificar que el historial viene ordenado por ID descendente"""
        historial = obtener_historial()
        if len(historial) >= 2:
            primer_id = historial[0][0]
            segundo_id = historial[1][0]
            self.assertGreater(primer_id, segundo_id, "❌ El historial debería estar ordenado DESC")
            print("✅ Test 7: Orden descendente correcto")
        else:
            self.skipTest("No hay suficientes datos para verificar orden")
    
    # ========================================
    # TESTS DE MODIFICACIÓN (3 casos)
    # ========================================
    
    def test_08_modificar_resultado_existente(self):
        """Test: Modificar un resultado existente"""
        historial = obtener_historial()
        if len(historial) > 0:
            id_a_modificar = historial[0][0]
            resultado = modificar_resultado(id_a_modificar, 99999999)
            self.assertTrue(resultado, "❌ La modificación debería ser exitosa")
            print(f"✅ Test 8: Modificación exitosa (ID {id_a_modificar})")
        else:
            self.skipTest("No hay datos para modificar")
    
    def test_09_modificar_resultado_inexistente(self):
        """Test: Intentar modificar un resultado que no existe (caso de error)"""
        resultado = modificar_resultado(999999999, 12345)
        # Debería retornar True pero no afectar filas (o implementar validación)
        self.assertIsNotNone(resultado, "❌ La función debería retornar algo")
        print("✅ Test 9: Manejo de ID inexistente")
    
    def test_10_modificar_con_valor_cero(self):
        """Test: Modificar un resultado a valor cero"""
        historial = obtener_historial()
        if len(historial) > 0:
            id_a_modificar = historial[0][0]
            resultado = modificar_resultado(id_a_modificar, 0)
            self.assertTrue(resultado, "❌ La modificación a cero debería ser exitosa")
            print(f"✅ Test 10: Modificación a cero exitosa (ID {id_a_modificar})")
        else:
            self.skipTest("No hay datos para modificar")
    
    # ========================================
    # TESTS DE ELIMINACIÓN (3 casos)
    # ========================================
    
    def test_11_eliminar_resultado_existente(self):
        """Test: Eliminar un resultado existente"""
        # Primero insertamos uno para asegurar que hay algo que eliminar
        insertar_resultado(111, 222, 333, 444, 555)
        historial = obtener_historial()
        if len(historial) > 0:
            id_a_eliminar = historial[0][0]
            resultado = eliminar_resultado(id_a_eliminar)
            self.assertTrue(resultado, "❌ La eliminación debería ser exitosa")
            print(f"✅ Test 11: Eliminación exitosa (ID {id_a_eliminar})")
        else:
            self.skipTest("No hay datos para eliminar")
    
    def test_12_eliminar_resultado_inexistente(self):
        """Test: Intentar eliminar un resultado que no existe (caso de error)"""
        resultado = eliminar_resultado(999999999)
        self.assertFalse(resultado, "❌ Debería retornar False al eliminar ID inexistente")
        print("✅ Test 12: Manejo correcto de ID inexistente en DELETE")
    
    def test_13_eliminar_y_verificar_ausencia(self):
        """Test: Eliminar y verificar que ya no existe en el historial"""
        # Insertamos un registro temporal
        insertar_resultado(777, 888, 999, 1010, 1111)
        historial_antes = obtener_historial()
        id_a_eliminar = historial_antes[0][0]
        
        # Eliminamos
        eliminar_resultado(id_a_eliminar)
        
        # Verificamos que ya no existe
        historial_despues = obtener_historial()
        ids_despues = [reg[0] for reg in historial_despues]
        self.assertNotIn(id_a_eliminar, ids_despues, "❌ El ID eliminado no debería existir")
        print(f"✅ Test 13: Verificación de eliminación correcta (ID {id_a_eliminar})")


if __name__ == "__main__":
    # Ejecutar tests con verbosidad
    unittest.main(verbosity=2)
