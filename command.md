pip freeze > requirements.txt
chmod +x ./entrypoint.sh
curl -i http://0.0.0.0:8000/

docker-compose up -d --build

./manage.py startapp taskapp

docker exec -it django /bin/sh

