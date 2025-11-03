"""Script para probar la conexión a PostgreSQL"""
import sys
import os

# Agregar la raíz del proyecto al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.db_conection import crear_conexion, crear_tabla

print("🔄 Probando conexión a PostgreSQL...")
conexion = crear_conexion()

if conexion:
    print("✅ Conexión exitosa!")
    conexion.close()
    
    print("\n🔄 Creando tablas...")
    crear_tabla()
else:
    print("❌ No se pudo conectar. Verifica SecretConfig.py")
