# test_django.py
import sys
import os

print("=== DIAGNÓSTICO DJANGO ===")
print("Directorio actual:", os.getcwd())
print("\nPython path:")
for path in sys.path:
    print("  ", path)

print("\n=== PRUEBA DE IMPORTACIÓN ===")
try:
    import django
    print("✅ Django importado correctamente")
    print("Versión:", django.__version__)
    
    from django.contrib import admin
    print("✅ django.contrib.admin importado correctamente")
    
except ImportError as e:
    print("❌ Error importando Django:", e)
    print("\n=== SOLUCIÓN ===")
    print("1. Activa el entorno virtual")
    print("2. Ejecuta: pip install django")
    print("3. Asegúrate de estar en la carpeta con manage.py")