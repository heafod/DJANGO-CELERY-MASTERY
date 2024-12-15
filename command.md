pip freeze > requirements.txt
chmod +x ./entrypoint.sh
curl -i http://0.0.0.0:8000/

docker-compose up -d --build

./manage.py startapp taskapp

docker exec -it django /bin/sh

# group
from newapp.tasks import tp1,tp2,tp3,tp4
task_groups = group(tp1.s(), tp2.s(), tp3.s(), tp4.s())
task_groups.apply_async()

