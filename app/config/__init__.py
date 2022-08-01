# imports Celery every time our application starts
from .celery import app as celery_app

__all__ = ('celery_app',)
