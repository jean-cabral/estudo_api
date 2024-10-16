#!/bin/sh

# Aplicando as migrações
python manage.py migrate

# Procurando fixtures e carregando-as
# for fixture in $(find ./apps -path "*/fixtures/*.json"); do
#   echo "Loading fixture: $fixture"
#   python manage.py loaddata $fixture
# done

# Iniciando o servidor Django
# exec gunicorn --bind 0.0.0.0:8000 core.wsgi:application
exec python manage.py runserver 0.0.0.0:8000