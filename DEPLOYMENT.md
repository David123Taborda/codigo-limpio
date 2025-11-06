# 🚀 Guía de Despliegue en Render

## Pasos para desplegar la aplicación en Render

### 1. Preparar el repositorio

Asegúrate de que tu repositorio tiene:
- ✅ `app.py` en la raíz
- ✅ `requirements.txt` en la raíz
- ✅ `SecretConfig.py` (con tus credenciales reales)
- ✅ Carpeta `templates/` con todos los HTML
- ✅ Carpeta `src/` con el código MVC

### 2. Subir cambios a GitHub

```bash
git add .
git commit -m "Preparado para despliegue en Render con Flask"
git push origin main
```

### 3. Crear Web Service en Render

1. Ve a [render.com](https://render.com) e inicia sesión
2. Haz clic en **"New +"** → **"Web Service"**
3. Conecta tu repositorio: `David123Taborda/codigo-limpio`

### 4. Configuración del Web Service

**Configuración básica:**
- **Name:** `calculadora-renta` (o el que prefieras)
- **Region:** `Oregon (US West)` o más cercana
- **Branch:** `main`
- **Root Directory:** (vacío)
- **Runtime:** `Python 3`

**Comandos:**
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`

**Plan:**
- Selecciona el plan **Free** (gratis)

### 5. Variables de Entorno (Opcional pero recomendado)

Si quieres mayor seguridad, agrega estas variables:

- `SECRET_KEY`: `tu_clave_secreta_aqui_muy_segura`
- `DB_HOST`: `dpg-d3ogr8bipnbc7380759g-a.virginia-postgres.render.com`
- `DB_PORT`: `5432`
- `DB_NAME`: `declaracionderenta`
- `DB_USER`: `juanydavid`
- `DB_PASSWORD`: `tu_password_aqui`

Y modifica `SecretConfig.py` para leer de variables de entorno:

```python
import os

DB_CONFIG = {
    'host': os.environ.get('DB_HOST', 'localhost'),
    'port': os.environ.get('DB_PORT', '5432'),
    'database': os.environ.get('DB_NAME', 'declaracionderenta'),
    'user': os.environ.get('DB_USER', 'usuario'),
    'password': os.environ.get('DB_PASSWORD', 'password')
}
```

### 6. Desplegar

1. Haz clic en **"Create Web Service"**
2. Espera 2-5 minutos mientras Render:
   - Clona tu repositorio
   - Instala las dependencias
   - Inicia la aplicación

### 7. Inicializar Base de Datos

Una vez desplegado:
1. Accede a tu URL: `https://tu-app.onrender.com`
2. Ve al menú **"🗄️ Crear Tablas"**
3. Haz clic en **"Crear Tablas en PostgreSQL"**

### 8. ¡Listo! 🎉

Tu aplicación está en línea y funcionando.

## Problemas Comunes

### Error: "Application failed to start"
- Verifica que `gunicorn` esté en `requirements.txt`
- Verifica que `app.py` esté en la raíz del proyecto
- Revisa los logs de Render para más detalles

### Error: "Database connection failed"
- Verifica que las credenciales de PostgreSQL sean correctas
- Asegúrate de que la base de datos en Render esté activa
- Verifica que el host sea accesible desde Render

### Error: "Module not found"
- Verifica que todas las dependencias estén en `requirements.txt`
- Usa `pip freeze > requirements.txt` para actualizar

## Actualizar la Aplicación

Cuando hagas cambios:

```bash
git add .
git commit -m "Descripción de los cambios"
git push origin main
```

Render detectará automáticamente los cambios y re-desplegará la aplicación.

---

¿Necesitas ayuda? Revisa los logs en el dashboard de Render.
