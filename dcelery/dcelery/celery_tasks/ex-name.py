from dcelery.celery_config import app


@app.task(queue="tasks")
def my_task1():
    return "task1"


@app.task(queue="tasks")
def my_task2():
    return "task2"
