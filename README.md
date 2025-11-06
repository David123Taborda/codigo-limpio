# 🧮 Calculadora de Declaración de Renta - Aplicación Web

Sistema web completo para calcular la base gravable del impuesto de renta en Colombia, desarrollado con Flask, PostgreSQL y desplegado en Render.

## 🌐 Aplicación Publicada

**URL de la aplicación:** [https://calculadora-de-renta.onrender.com](https://calculadora-de-renta.onrender.com)

---

## 🔗 Enlaces del Proyecto

- **Audios de entrevista:** [Google Drive](https://drive.google.com/drive/folders/1Px86WvVIzanwdtUpdDr4zCUoKNaw0uHq?usp=drive_link)
- **Casos de uso:** [Excel SharePoint](https://udemedellin-my.sharepoint.com/:x:/r/personal/dtaborda789_soyudemedellin_edu_co/Documents/calculadora%20de%20impuestos.xlsx?d=wea0377cbd11e4fd199019b71ff3f5436&csf=1&web=1&e=6WGpY6)
- **Repositorio GitHub:** [https://github.com/David123Taborda/codigo-limpio](https://github.com/David123Taborda/codigo-limpio)

---

## ✨ Características

### Funcionalidades Web Implementadas

✅ **Funcionalidad Web Principal:** Cálculo de base gravable con inserción automática en BD  
✅ **Funcionalidad Web para Buscar:** Consulta y visualización del historial de cálculos  
✅ **Funcionalidad Web para Insertar:** Formulario de entrada y guardado de resultados  
✅ **Funcionalidad Web para Modificar:** Edición de registros existentes  
✅ **Menú de Inicio:** Navegación intuitiva entre todas las funcionalidades  
✅ **Opción para Crear Tablas:** Inicialización de la base de datos desde la interfaz  
✅ **Arquitectura MVC con Blueprints de Flask:** Código organizado y mantenible  
✅ **Pruebas Unitarias:** 26 casos de prueba completos  

### Tecnologías Utilizadas

- **Backend:** Flask 3.0.0 (Python)
- **Base de Datos:** PostgreSQL (Render Cloud)
- **Frontend:** HTML5 + CSS3 (sin frameworks externos)
- **Servidor:** Gunicorn para producción
- **Despliegue:** Render Web Service

---

---

## � Estructura del Proyecto (MVC con Blueprints)

```
codigo-limpio/
│
├── app.py                          # Aplicación Flask principal
├── requirements.txt                # Dependencias del proyecto
├── SecretConfig.py                 # Configuración de la base de datos
├── README.md                       # Este archivo
│
├── templates/                      # Vistas HTML (Frontend)
│   ├── base.html                  # Template base con estilos
│   ├── index.html                 # Menú principal
│   ├── calcular.html              # Formulario de cálculo (Insertar)
│   ├── resultado.html             # Visualización de resultados
│   ├── buscar.html                # Historial y búsqueda
│   ├── modificar.html             # Edición de registros
│   └── crear_tablas.html          # Configuración de BD
│
├── src/                           # Código fuente (Modelo-Controlador)
│   ├── __init__.py
│   ├── db_conection.py            # Conexión y operaciones CRUD
│   │
│   ├── model/                     # Modelos (Lógica de negocio)
│   │   ├── __init__.py
│   │   └── Calculadora.py         # Cálculos de impuestos
│   │
│   ├── controller/                # Controladores
│   │   ├── CalculadoraController.py
│   │   └── controller.py
│   │
│   └── routes/                    # Blueprints de Flask (Rutas)
│       ├── __init__.py
│       ├── calculadora_routes.py  # Rutas de cálculo y CRUD
│       └── database_routes.py     # Rutas de configuración de BD
│
└── tests/                         # Pruebas Unitarias
    ├── test_Calculadora.py        # Tests del modelo
    ├── test_conexion.py           # Tests de conexión
    ├── test_crud_database.py      # Tests de operaciones CRUD
    └── test_db.py                 # Tests de base de datos
```

---

## 🚀 Instrucciones para Ejecutar Localmente

### 1️⃣ Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- PostgreSQL instalado (opcional, se puede usar Render)

### 2️⃣ Clonar el Repositorio

```bash
git clone https://github.com/David123Taborda/codigo-limpio.git
cd codigo-limpio
```

### 3️⃣ Crear Entorno Virtual

```bash
# En Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# En Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 4️⃣ Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 5️⃣ Configurar Base de Datos

#### Opción A: Usar PostgreSQL en Render (Recomendado)

1. El archivo `SecretConfig.py` ya está configurado con la conexión a Render
2. No necesitas hacer nada adicional

#### Opción B: Usar PostgreSQL Local (Base de Datos en Blanco)

1. Instala PostgreSQL en tu máquina
2. Crea una base de datos nueva:
   ```sql
   CREATE DATABASE declaracionderenta;
   ```
3. Edita el archivo `SecretConfig.py`:
   ```python
   DB_CONFIG = {
       'host': 'localhost',
       'port': '5432',
       'database': 'declaracionderenta',
       'user': 'tu_usuario',
       'password': 'tu_contraseña'
   }
   ```

### 6️⃣ Crear las Tablas en la Base de Datos

Tienes dos opciones:

**Opción A: Desde la interfaz web**
1. Ejecuta la aplicación (paso 7)
2. Ve a la opción "🗄️ Crear Tablas" en el menú
3. Haz clic en "Crear Tablas en PostgreSQL"

**Opción B: Desde Python**
```bash
python -c "from src.db_conection import crear_tabla; crear_tabla()"
```

### 7️⃣ Ejecutar la Aplicación

```bash
python app.py
```

La aplicación estará disponible en: **http://localhost:5000**

### 8️⃣ Navegación por la Aplicación

1. **Página de Inicio** (`/`): Menú principal con acceso a todas las funcionalidades
2. **Calcular** (`/calculadora/calcular`): Formulario para calcular e insertar resultados
3. **Buscar** (`/calculadora/buscar`): Ver historial, modificar y eliminar registros
4. **Crear Tablas** (`/database/crear-tablas`): Inicializar la base de datos

---

## 🧪 Ejecutar Pruebas Unitarias

```bash
# Ejecutar todos los tests
python -m unittest discover tests

# Ejecutar un test específico
python -m unittest tests.test_Calculadora
python -m unittest tests.test_conexion
python -m unittest tests.test_crud_database
```

**Estado actual:** ✅ 26 pruebas pasando correctamente

---

## 🌐 Despliegue en Render

### Paso 1: Preparar el Repositorio

1. Asegúrate de que `requirements.txt` y `app.py` estén en la raíz del proyecto ✅
2. Commit y push todos los cambios a GitHub:
   ```bash
   git add .
   git commit -m "Preparado para despliegue en Render"
   git push origin main
   ```

### Paso 2: Crear Web Service en Render

1. Ve a [render.com](https://render.com) e inicia sesión
2. Haz clic en **"New +"** → **"Web Service"**
3. Conecta tu repositorio de GitHub: `David123Taborda/codigo-limpio`
4. Configura los siguientes parámetros:

   - **Name:** `calculadora-renta` (o el nombre que prefieras)
   - **Region:** `Oregon (US West)` o la más cercana
   - **Branch:** `main`
   - **Root Directory:** (dejar vacío)
   - **Runtime:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`

5. **Variables de Entorno** (opcional):
   - Agregar `SECRET_KEY` con un valor seguro
   - Si usas otra BD, agregar las variables de conexión

6. Haz clic en **"Create Web Service"**

### Paso 3: Esperar el Despliegue

- Render instalará las dependencias y ejecutará la aplicación
- El proceso toma aproximadamente 2-5 minutos
- Una vez completado, verás la URL de tu aplicación: `https://tu-app.onrender.com`

### Paso 4: Inicializar la Base de Datos

1. Accede a tu aplicación desplegada
2. Ve a la opción **"🗄️ Crear Tablas"** en el menú
3. Haz clic en **"Crear Tablas en PostgreSQL"**
4. ¡Listo! Tu aplicación está funcionando en la web

---

## 📊 Descripción del Cálculo

### Entradas del Sistema

- **Sueldo mensual** → Salario fijo percibido mensualmente
- **Otros ingresos** → Ganancias adicionales (honorarios, rentas, inversiones)
- **Aporte a pensión** → Valor anual aportado al sistema de pensiones
- **Intereses crédito vivienda** → Intereses pagados por préstamo hipotecario (deducibles)
- **Gastos médicos** → Gastos médicos deducibles
- **Personas a cargo** → Número de dependientes económicos
- **Patrimonio** → Valor total del patrimonio del contribuyente

### Proceso de Cálculo

1. **Ingreso total anual** = (Sueldo × 12) + Auxilio transporte ($6,000,000) + Otros ingresos
2. **Deducciones por ley** = Aporte pensión + Deducción fija ($3,000,000)
3. **Deducciones personales** = Crédito vivienda + Gastos médicos
4. **Renta exenta** = 25% × (Ingresos - Deducciones ley)
5. **Base gravable** = Ingresos - Deducciones ley - Deducciones personales - Renta exenta

### 📤 Salidas

- Ingreso total anual
- Deducciones por ley
- Deducciones personales
- Renta exenta (25%)
- **Base gravable** (sobre la que se paga impuesto)

2. **Deducciones de ley** = Aporte pensión + $3,000,000 (fijo por ley)
3. **Deducciones personales** = Crédito vivienda + Gastos médicos
4. **Renta exenta** = 25% × (Ingreso total - Deducciones de ley)
5. **Base gravable** = Ingreso total - Deducciones de ley - Deducciones personales - Renta exenta

### Salida

- **Base gravable:** Monto sobre el cual se calculará el impuesto de renta según tarifas de la DIAN

---

## 🛠️ Arquitectura MVC con Blueprints

### Modelo (`src/model/`)
- **Calculadora.py:** Funciones puras para cálculos de impuestos
- Sin dependencias de Flask ni base de datos

### Vista (`templates/`)
- **Templates HTML:** Interfaz de usuario con Jinja2
- **CSS integrado:** Estilos responsivos sin frameworks externos

### Controlador (`src/controller/` + `src/routes/`)
- **CalculadoraController.py:** Lógica de negocio y coordinación
- **calculadora_routes.py:** Blueprint con rutas de CRUD
- **database_routes.py:** Blueprint para configuración de BD

### Base de Datos (`src/db_conection.py`)
- Operaciones CRUD con PostgreSQL
- Manejo de errores y conexiones seguras

---

## 📝 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

## 👨‍💻 Autor

**David Taborda & Juan Camilo**  
Universidad de Medellín - Ingeniería de Software  
2025

---

## 📞 Soporte

Si tienes problemas con el despliegue o la ejecución:

1. Verifica que `requirements.txt` tenga las dependencias correctas
2. Confirma que la conexión a PostgreSQL esté activa
3. Revisa los logs en Render para identificar errores
4. Asegúrate de haber creado las tablas antes de usar la aplicación

---

¡Gracias por usar la Calculadora de Declaración de Renta! 🎉

1. Abre el archivo `SecretConfig.py`
2. **⚠️ NO subas este archivo a GitHub** (ya está en `.gitignore`)
3. Configura con tus credenciales de PostgreSQL:

```python
DB_CONFIG = {
    'host': 'tu-host.render.com',
    'port': '5432',
    'database': 'tu_base_de_datos',
    'user': 'tu_usuario',
    'password': 'tu_contraseña'
}
```

### **Paso 5: Crear tablas**
```powershell
python tests/test_conexion.py
```

---

## 🎮 Uso del Sistema

### **Ejecutar la aplicación:**
```powershell
python src/ui/gui.py
```

### **Funcionalidades disponibles:**

1. **Calcular Impuesto** → Ingresa datos y obtén la base gravable (se guarda automáticamente)
2. **Ver Historial** → Consulta los últimos 10 cálculos realizados
3. **Modificar Último Resultado** → Corrige el último cálculo guardado
4. **Eliminar Último Resultado** → Elimina el último registro (con confirmación)

---

## 🧪 Ejecutar Tests

### **Tests del modelo (lógica de negocio):**
```powershell
python -m unittest tests.test_Calculadora -v
```

### **Tests CRUD (base de datos):**
```powershell
python tests/test_crud_database.py
```

**Cobertura total:** 26 tests (13 modelo + 13 CRUD)

---

## 📁 Estructura del Proyecto

```
codigo-limpio/
├── src/
│   ├── model/
│   │   └── Calculadora.py          # Lógica de negocio y validaciones
│   ├── controller/
│   │   └── CalculadoraController.py # Controlador MVC
│   ├── ui/
│   │   └── gui.py                   # Interfaz gráfica Kivy
│   ├── view/
│   │   └── Interfaz_Calculadora.py  # Interfaz CLI (legacy)
│   └── db_conection.py              # Conexión PostgreSQL + CRUD
│
├── tests/
│   ├── test_Calculadora.py          # Tests lógica de negocio (13)
│   ├── test_crud_database.py        # Tests CRUD PostgreSQL (13)
│   └── test_conexion.py             # Test de conexión
│
├── SecretConfig.py                  # ⚠️ Credenciales (NO SUBIR A GIT)
├── .gitignore                       # Ignora archivos sensibles
└── README.md                        # Este archivo
```

---

## 🔧 Tecnologías Utilizadas

- **Python 3.13** - Lenguaje principal
- **Kivy 2.3.1** - Interfaz gráfica multiplataforma
- **PostgreSQL** - Base de datos en la nube (Render)
- **psycopg2-binary** - Driver de PostgreSQL para Python
- **unittest** - Framework de testing

---

## 📊 Operaciones CRUD Implementadas

| Operación | Función | Archivo | Interfaz |
|-----------|---------|---------|----------|
| **CREATE** | `crear_tabla()` | `db_conection.py` | Automático al iniciar |
| **INSERT** | `insertar_resultado()` | `db_conection.py` | Botón "Calcular" |
| **SELECT** | `obtener_historial()` | `db_conection.py` | Botón "Ver historial" |
| **UPDATE** | `modificar_resultado()` | `db_conection.py` | Botón "Modificar último" |
| **DELETE** | `eliminar_resultado()` | `db_conection.py` | Botón "Eliminar último" |

---

## 🐛 Solución de Problemas

### **Error: `ModuleNotFoundError: No module named 'kivy'`**
```powershell
# Activa el entorno virtual
.\.venv313\Scripts\Activate.ps1
pip install kivy
```

### **Error: `No module named 'psycopg2'`**
```powershell
pip install psycopg2-binary
```

### **Error: `password authentication failed`**
- Verifica credenciales en `SecretConfig.py`
- Asegúrate de usar el host correcto (Virginia, Oregon, etc.)

---

## 👥 Créditos

**Desarrollo:**
- **David Taborda** - [@David123Taborda](https://github.com/David123Taborda)
- **Juan Ocampo** - Colaborador

**Diseño de Interfaz Original:**
- Cristian Copete
- Susana Morales

**Institución:** Universidad de Medellín

---

## ✨ Estado del Proyecto

🎉 **PROYECTO COMPLETO Y FUNCIONAL**

✅ Operaciones CRUD completas (CREATE, INSERT, SELECT, UPDATE, DELETE)  
✅ 26 tests unitarios pasando exitosamente  
✅ Interfaz gráfica Kivy operativa  
✅ Base de datos PostgreSQL en producción (Render)  
✅ Arquitectura MVC implementada  
✅ Documentación completa  

---

## 📄 Licencia

Este proyecto es de uso académico para la Universidad de Medellín. 
      

