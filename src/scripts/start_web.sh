#sh /src/scripts/wait.sh

cd /src
# collectstatic needs DJANGO_SETTINGS_MODULE
export DJANGO_SETTINGS_MODULE=ecoquartier.settings
pip install pillow
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py makemessages -a
python manage.py compilemessages
uwsgi --socket :8000 --wsgi-file /src/ecoquartier/wsgi.py --chdir /src/ecoquartier --master --processes 4 --threads 2 --py-autoreload 3
