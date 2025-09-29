#!/usr/bin/env bash
# exit on error
set -o errexit

echo "=== INSTALANDO DEPENDENCIAS ==="
pip install -r requirements.txt

echo "=== VERIFICANDO ENTORNO ==="
python -c "
import os
print('DEBUG:', os.environ.get('DEBUG'))
print('DATABASE_URL:', os.environ.get('DATABASE_URL'))
print('CLOUDINARY_CLOUD_NAME:', os.environ.get('CLOUDINARY_CLOUD_NAME'))
"

echo "=== VERIFICANDO ARCHIVOS ESTÁTICOS DEL ADMIN ==="
python -c "
import django
print('Django path:', django.__path__[0])
import os
admin_path = os.path.join(django.__path__[0], 'contrib/admin/static/admin')
print('Admin static exists:', os.path.exists(admin_path))
if os.path.exists(admin_path):
    print('Admin CSS exists:', os.path.exists(os.path.join(admin_path, 'css/base.css')))
"

echo "=== EJECUTANDO COLLECTSTATIC ==="
python manage.py collectstatic --noinput --verbosity 2

echo "=== VERIFICANDO RESULTADO ==="
ls -la staticfiles/ || echo "staticfiles/ no existe"
find staticfiles/ -name '*.css' | head -5 || echo "No CSS files found"

echo "=== APLICANDO MIGRACIONES ==="
python manage.py migrate


