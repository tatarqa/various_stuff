from random import randint
from time import sleep
from celery import Celery

# Start a celery instance
celery = Celery('tasks', broker='redis://localhost:6379/9', backend='redis://localhost:6379/10')


@celery.task
def slow_add(num1, num2):
    """
    Slowly add two numbers, replicating a long-running task.

    :param num1: First digit to add
    :param num2: Second digit to add
    :return: Sum of num1 and num2
    """

    sleep(10)

    # Sum and return
    return num1 + num2
