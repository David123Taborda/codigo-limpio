"""
Script para verificar que el proyecto está listo para desplegar en Render
"""
import os
import sys

def check_file_exists(filename, description):
    """Verifica si un archivo existe"""
    if os.path.exists(filename):
        print(f"✅ {description}: {filename}")
        return True
    else:
        print(f"❌ FALTA: {description}: {filename}")
        return False

def check_directory_exists(dirname, description):
    """Verifica si un directorio existe"""
    if os.path.isdir(dirname):
        print(f"✅ {description}: {dirname}")
        return True
    else:
        print(f"❌ FALTA: {description}: {dirname}")
        return False

def main():
    print("=" * 60)
    print("🔍 VERIFICACIÓN PRE-DESPLIEGUE EN RENDER")
    print("=" * 60)
    print()
    
    all_ok = True
    
    print("📄 Archivos principales:")
    all_ok &= check_file_exists("app.py", "Aplicación Flask principal")
    all_ok &= check_file_exists("requirements.txt", "Dependencias")
    all_ok &= check_file_exists("SecretConfig.py", "Configuración de BD")
    all_ok &= check_file_exists("README.md", "Documentación")
    print()
    
    print("📁 Estructura de directorios:")
    all_ok &= check_directory_exists("templates", "Vistas HTML")
    all_ok &= check_directory_exists("src", "Código fuente")
    all_ok &= check_directory_exists("src/model", "Modelos")
    all_ok &= check_directory_exists("src/controller", "Controladores")
    all_ok &= check_directory_exists("src/routes", "Blueprints")
    all_ok &= check_directory_exists("tests", "Pruebas unitarias")
    print()
    
    print("📝 Templates HTML:")
    templates = [
        "base.html", "index.html", "calcular.html", 
        "resultado.html", "buscar.html", "modificar.html", "crear_tablas.html"
    ]
    for template in templates:
        all_ok &= check_file_exists(f"templates/{template}", f"Template {template}")
    print()
    
    print("🔧 Verificando requirements.txt:")
    try:
        with open("requirements.txt", "r") as f:
            content = f.read()
            required = ["Flask", "psycopg2-binary", "gunicorn"]
            for req in required:
                if req in content:
                    print(f"✅ Dependencia encontrada: {req}")
                else:
                    print(f"❌ FALTA dependencia: {req}")
                    all_ok = False
    except Exception as e:
        print(f"❌ Error al leer requirements.txt: {e}")
        all_ok = False
    print()
    
    print("🧪 Verificando tests:")
    try:
        import unittest
        loader = unittest.TestLoader()
        suite = loader.discover('tests')
        test_count = suite.countTestCases()
        print(f"✅ {test_count} pruebas unitarias encontradas")
    except Exception as e:
        print(f"⚠️ No se pudieron cargar los tests: {e}")
    print()
    
    print("=" * 60)
    if all_ok:
        print("✅ ¡TODO LISTO PARA DESPLEGAR EN RENDER!")
        print()
        print("📋 Siguientes pasos:")
        print("1. git add .")
        print('2. git commit -m "Preparado para despliegue"')
        print("3. git push origin main")
        print("4. Ve a render.com y crea un nuevo Web Service")
        print("5. Conecta tu repositorio GitHub")
        print("6. Configura Build Command: pip install -r requirements.txt")
        print("7. Configura Start Command: gunicorn app:app")
        print("8. Despliega y espera 2-5 minutos")
        print()
        return 0
    else:
        print("❌ HAY PROBLEMAS QUE RESOLVER ANTES DE DESPLEGAR")
        print("Por favor corrige los errores marcados arriba")
        print()
        return 1

if __name__ == "__main__":
    sys.exit(main())
