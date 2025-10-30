from src.db_conection import crear_conexion
from src.db_conection import crear_conexion

if __name__ == "__main__":
    conexion = crear_conexion()
    if conexion:
        print("✅ Conexión establecida correctamente.")
    else:
        print("❌ Error al conectar.")
