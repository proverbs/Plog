# Plog
a blog system using python flask

initialize database:
python manage.py db init
python manage.py db migrate -m "initial migration"
python manage.py db upgrade

deploy database:
python manage.py deploy

run app:
python manage.py runserver
