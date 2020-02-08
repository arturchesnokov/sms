from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sms.settings')

app = Celery('sms')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# Celery application definition
# http://docs.celeryproject.org/en/v4.0.2/userguide/configuration.html
# CELERY_BROKER_URL = 'amqp://guest:**@localhost:5672'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379'
app.conf.accept_content = ['application/json']
app.conf.result_serializer = 'json'
app.conf.task_serializer = 'json'
app.conf.timezone = 'UTC'

app.conf.beat_schedule = {
    'cleaning-old-data': {
        'task': 'students.tasks.clean_old_data',
        'schedule': crontab(minute=0, hour=0),  # every day at midnight
        'args': (2,)  # days - logger data older then this q-ty of days will  be removed
    }
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
