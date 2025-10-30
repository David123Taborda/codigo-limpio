import sqlite3
import os

# ===============================
# CONFIGURACIÓN DE LA BASE DE DATOS
# ===============================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(DB_DIR, "calculadora.db")

def crear_conexion():
    """Crea y retorna una conexión a la base de datos calculadora.db"""
    try:
        os.makedirs(DB_DIR, exist_ok=True)
        conexion = sqlite3.connect(DB_PATH)
        print("✅ Conexión establecida con la base de datos")
        return conexion
    except sqlite3.Error as e:
        print(f"❌ Error de conexión: {e}")
        return None


def crear_tabla():
    """Crea las tablas necesarias si no existen"""
    conexion = crear_conexion()
    if not conexion:
        print("❌ No se pudo crear la tabla porque la conexión falló.")
        return

    cursor = conexion.cursor()
    # Tabla principal de historial de cálculos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS historial_calculos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sueldo REAL,
            otros_ingresos REAL,
            aporte_pension REAL,
            credito_vivienda REAL,
            gasto_medicina REAL,
            personas_a_cargo INTEGER,
            patrimonio REAL,
            base_gravable REAL
        )
    """)
    # Tabla de resultados simples
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resultados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            operacion TEXT,
            resultado REAL
        )
    """)
    conexion.commit()
    conexion.close()
    print("✅ Tablas creadas correctamente.")


# ===============================
# OPERACIONES CRUD
# ===============================

def insertar_resultado(operacion, resultado):
    """Inserta un nuevo resultado en la tabla resultados"""
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO resultados (operacion, resultado) VALUES (?, ?)", (operacion, resultado))
    conexion.commit()
    conexion.close()
    print(f"✅ Resultado '{operacion}' = {resultado} insertado correctamente.")


def obtener_historial():
    """Obtiene los últimos 10 registros del historial de cálculos"""
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM historial_calculos ORDER BY id DESC LIMIT 10")
    filas = cursor.fetchall()
    conexion.close()
    return filas


def modificar_resultado(id_resultado, nuevo_resultado):
    """Actualiza el valor de un resultado por su ID"""
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute("UPDATE resultados SET resultado = ? WHERE id = ?", (nuevo_resultado, id_resultado))
    conexion.commit()
    conexion.close()
    print(f"✏️ Resultado con ID {id_resultado} modificado a {nuevo_resultado}.")


if __name__ == "__main__":
    crear_tabla()
