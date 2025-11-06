# Configuración de PostgreSQL en Render
# INSTRUCCIONES:
# 1. Copia este archivo como "SecretConfig.py"
# 2. Reemplaza los valores con tus credenciales reales de PostgreSQL

DB_CONFIG = {
    'host': 'tu-host.render.com',  # Ejemplo: dpg-xxxxx-a.virginia-postgres.render.com
    'port': '5432',
    'database': 'nombre_de_tu_base_de_datos',
    'user': 'tu_usuario',
    'password': 'tu_contraseña_segura'
}
