```angular2html
python3 -m venv venv
source venv/bin/activate

pip install django
django-admin startproject dcelery .

pip freeze > requirements.txt

pip install celery
pip install redis
```# DJANGO-CELERY-MASTERY
