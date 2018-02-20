from __future__ import absolute_import
from conf.celery import app


@app.task(name='proj.tasks.minus')
def minus(x, y):
    return x - y
