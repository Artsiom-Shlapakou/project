import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
 
app = Celery(__name__)
app.config_from_object('django.conf:settings')
 
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'run-every-day-morning': {
        'task': 'providers.tasks.reduce_debt',
        'schedule': crontab(hour=6, minute=30, day_of_week='*'),
    },
    'run-every-three-hour': {
        'task': 'providers.tasks.increase_debt',
        'schedule': crontab(minute=0, hour='*/3'),
    },
}
