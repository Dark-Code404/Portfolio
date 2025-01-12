web: python manage.py migrate && python manage.py collectstatic --noinput && gunicorn Portfolio_website.wsgi --log-file - --log-level debug --bind 0.0.0.0:$PORT
