# 🧮 Calculadora de Declaración de Renta

Sistema completo para calcular la base gravable del impuesto de renta en Colombia, con interfaz gráfica Kivy y base de datos PostgreSQL en la nube.

## 🔗 Enlaces del Proyecto

- **Audios de entrevista:** [Google Drive](https://drive.google.com/drive/folders/1Px86WvVIzanwdtUpdDr4zCUoKNaw0uHq?usp=drive_link)
- **Casos de uso:** [Excel SharePoint](https://udemedellin-my.sharepoint.com/:x:/r/personal/dtaborda789_soyudemedellin_edu_co/Documents/calculadora%20de%20impuestos.xlsx?d=wea0377cbd11e4fd199019b71ff3f5436&csf=1&web=1&e=6WGpY6)

---

## � Características

✅ **Operaciones CRUD completas:**
- ✅ CREATE TABLE - Creación de tablas en PostgreSQL
- ✅ INSERT - Inserción de resultados calculados
- ✅ SELECT - Consulta de historial (últimos 10 registros)
- ✅ UPDATE - Modificación de registros existentes
- ✅ DELETE - Eliminación de registros

✅ **Interfaz gráfica con Kivy:**
- Formulario de entrada de datos fiscales
- Cálculo automático de base gravable
- Visualización de historial de cálculos
- Modificación y eliminación de registros

✅ **Base de datos PostgreSQL en Render (nube)**  
✅ **Tests unitarios completos (26 casos de prueba)**  
✅ **Arquitectura MVC limpia**

---

## 📄 Descripción del Cálculo

Este sistema calcula la base sobre la que se paga impuesto de renta para personas naturales a partir de sus ingresos, deducciones y beneficios tributarios.

### 📥 Entradas
El sistema recibe las siguientes variables para cada caso:

- **Sueldo mensual** → Salario fijo percibido mensualmente
- **Otros ingresos** → Ganancias adicionales (honorarios, rentas, inversiones)
- **Aporte a pensión** → Valor anual aportado al sistema de pensiones
- **Intereses crédito vivienda** → Intereses pagados por préstamo hipotecario (deducibles)
- **Gastos médicos** → Gastos médicos deducibles
- **Personas a cargo** → Número de dependientes económicos
- **Patrimonio** → Valor total del patrimonio del contribuyente

### ⚙️ Proceso de Cálculo

1. **Ingreso total anual** = (Sueldo × 12) + Auxilio transporte + Otros ingresos
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

---
## 🚀 Instalación y Configuración

### **Paso 1: Clonar el repositorio**
```bash
git clone https://github.com/David123Taborda/codigo-limpio.git
cd codigo-limpio
```

### **Paso 2: Crear entorno virtual con Python 3.13**
```powershell
# Windows PowerShell
py -3.13 -m venv .venv313

# Activar el entorno virtual
.\.venv313\Scripts\Activate.ps1

# Si da error de ejecución de scripts:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### **Paso 3: Instalar dependencias**
```powershell
pip install kivy psycopg2-binary
```

### **Paso 4: Configurar base de datos**

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
      

