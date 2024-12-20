import time

from celery import shared_task


@shared_task
def task1():
    return


@shared_task()
def task2():
    return


@shared_task(task_rate_limit="10/m")
def tp1(queue="celery"):
    time.sleep(5)
    return "TP1"


@shared_task
def tp2(queue="celery:1"):
    time.sleep(5)
    return "TP2"


@shared_task
def tp3(queue="celery:2"):
    time.sleep(5)
    return "TP3"


@shared_task
def tp4(queue="celery:3"):
    time.sleep(5)
    return "TP4"
