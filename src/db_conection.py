import psycopg2
from psycopg2 import sql, Error
from SecretConfig import DB_CONFIG

# ===============================
# CONFIGURACIÓN DE LA BASE DE DATOS POSTGRESQL
# ===============================

def crear_conexion():
    """Crea y retorna una conexión a la base de datos PostgreSQL en Render"""
    try:
        conexion = psycopg2.connect(
            host=DB_CONFIG['host'],
            port=DB_CONFIG['port'],
            database=DB_CONFIG['database'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password']
        )
        print("✅ Conexión establecida con PostgreSQL")
        return conexion
    except Error as e:
        print(f"❌ Error de conexión a PostgreSQL: {e}")
        return None


def crear_tabla():
    """Crea las tablas necesarias si no existen (PostgreSQL)"""
    conexion = crear_conexion()
    if not conexion:
        print("❌ No se pudo crear la tabla porque la conexión falló.")
        return

    cursor = conexion.cursor()
    # Tabla principal de historial de cálculos (PostgreSQL usa SERIAL en lugar de AUTOINCREMENT)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS historial_calculos (
            id SERIAL PRIMARY KEY,
            sueldo REAL,
            otros_ingresos REAL,
            aporte_pension REAL,
            credito_vivienda REAL,
            gasto_medicina REAL,
            personas_a_cargo INTEGER,
            patrimonio REAL,
            base_gravable REAL,
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    # Tabla de resultados simples
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resultados (
            id SERIAL PRIMARY KEY,
            ingreso_total REAL,
            deducciones_ley REAL,
            deducciones_personales REAL,
            renta_exenta REAL,
            base_gravable REAL,
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conexion.commit()
    conexion.close()
    print("✅ Tablas creadas correctamente en PostgreSQL.")


# ===============================
# OPERACIONES CRUD
# ===============================

def insertar_resultado(ingreso_total, deducciones_ley, deducciones_personales, renta_exenta, base_gravable):
    """Inserta un nuevo resultado en la tabla resultados (PostgreSQL usa %s en lugar de ?)"""
    conexion = crear_conexion()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO resultados 
            (ingreso_total, deducciones_ley, deducciones_personales, renta_exenta, base_gravable)
            VALUES (%s, %s, %s, %s, %s)
        """, (ingreso_total, deducciones_ley, deducciones_personales, renta_exenta, base_gravable))
        conexion.commit()
        conexion.close()
        print(f"✅ Resultado insertado: Base gravable = ${base_gravable:,.2f}")
        return True
    except Error as e:
        print(f"❌ Error al insertar: {e}")
        conexion.close()
        return False


def obtener_historial():
    """Obtiene los últimos 10 registros del historial (PostgreSQL)"""
    conexion = crear_conexion()
    if not conexion:
        return []
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT id, ingreso_total, deducciones_ley, deducciones_personales, 
                   renta_exenta, base_gravable, fecha_creacion
            FROM resultados 
            ORDER BY id DESC 
            LIMIT 10
        """)
        filas = cursor.fetchall()
        conexion.close()
        return filas
    except Error as e:
        print(f"❌ Error al obtener historial: {e}")
        conexion.close()
        return []


def modificar_resultado(id_resultado, nuevo_base_gravable):
    """Actualiza el valor de base_gravable por su ID (PostgreSQL usa %s)"""
    conexion = crear_conexion()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE resultados SET base_gravable = %s WHERE id = %s", 
            (nuevo_base_gravable, id_resultado)
        )
        conexion.commit()
        conexion.close()
        print(f"✏️ Resultado con ID {id_resultado} modificado a ${nuevo_base_gravable:,.2f}")
        return True
    except Error as e:
        print(f"❌ Error al modificar: {e}")
        conexion.close()
        return False


def eliminar_resultado(id_resultado):
    """Elimina un resultado por su ID (DELETE)"""
    conexion = crear_conexion()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM resultados WHERE id = %s", (id_resultado,))
        conexion.commit()
        filas_afectadas = cursor.rowcount
        conexion.close()
        if filas_afectadas > 0:
            print(f"🗑️ Resultado con ID {id_resultado} eliminado correctamente")
            return True
        else:
            print(f"⚠️ No se encontró ningún resultado con ID {id_resultado}")
            return False
    except Error as e:
        print(f"❌ Error al eliminar: {e}")
        conexion.close()
        return False


if __name__ == "__main__":
    crear_tabla()
