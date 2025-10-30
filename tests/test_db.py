import sqlite3
import os
import pytest

# ===============================
# FIXTURE PRINCIPAL: BASE DE DATOS
# ===============================

@pytest.fixture(scope="module")
def conexion():
    """
    Crea una conexión temporal a la base de datos calculadora.db.
    Si las tablas no existen, las crea.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(base_dir, "data", "calculadora.db")
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Crear tablas necesarias
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
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resultados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            operacion TEXT,
            resultado REAL
        )
    """)
    conn.commit()
    yield conn
    conn.close()


# ======================================
# 1️⃣ PRUEBAS DE INSERCIÓN (3 casos)
# ======================================

def test_insertar_historial(conexion):
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO historial_calculos (sueldo, otros_ingresos, aporte_pension, credito_vivienda,
                                        gasto_medicina, personas_a_cargo, patrimonio, base_gravable)
        VALUES (2000000, 500000, 150000, 200000, 80000, 2, 10000000, 2300000)
    """)
    conexion.commit()
    cursor.execute("SELECT COUNT(*) FROM historial_calculos")
    assert cursor.fetchone()[0] > 0


def test_insertar_resultado(conexion):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO resultados (operacion, resultado) VALUES (?, ?)", ("suma", 42))
    conexion.commit()
    cursor.execute("SELECT * FROM resultados WHERE operacion='suma'")
    data = cursor.fetchone()
    assert data is not None
    assert data[2] == 42


def test_insertar_varios_resultados(conexion):
    cursor = conexion.cursor()
    datos = [("resta", 15), ("multiplicación", 120), ("división", 5)]
    cursor.executemany("INSERT INTO resultados (operacion, resultado) VALUES (?, ?)", datos)
    conexion.commit()
    cursor.execute("SELECT COUNT(*) FROM resultados")
    assert cursor.fetchone()[0] >= 3


# ======================================
# 2️⃣ PRUEBAS DE BÚSQUEDA (3 casos)
# ======================================

def test_buscar_historial(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT sueldo FROM historial_calculos LIMIT 1")
    resultado = cursor.fetchone()
    assert resultado is not None


def test_buscar_resultado_por_operacion(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT resultado FROM resultados WHERE operacion='suma'")
    res = cursor.fetchone()
    assert res[0] == 42


def test_buscar_todos_resultados(conexion):
    cursor = conexion.cursor
