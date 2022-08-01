import random
from config.celery import app
from celery import Task, shared_task

from django.db.models import F
from providers.models import Provider
from providers.utils import set_debt


@app.task
def reduce_debt():
    objects_with_debt = Provider.objects.filter(debt_gt=0)
    [set_debt(obj) for obj in objects_with_debt]
    Provider.objects.bulk_update(objects_with_debt, ["debt"])


@app.task
def increase_debt():
    increasion_value = random.randint(5, 500)
    Provider.objects.update(debt=F('debt') + increasion_value)
