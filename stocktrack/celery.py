from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
# from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stocktrack.settings')

app = Celery('stocktrack')
app.conf.enable_utc = False
app.conf.update(timezone = 'Africa/Nairobi')

app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
    'every-10-seconds' : {
        'task': 'stocks.tasks.update',
        'schedule': 10,
        'args': (['RELIANCE.NS', 'BAJAJ-AUTO.NS'],)
    }, 
}

app.autodiscover_tasks()

app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')