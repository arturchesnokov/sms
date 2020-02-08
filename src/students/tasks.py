from celery import shared_task, task
from time import sleep
from datetime import datetime, timedelta, timezone

from django.core.mail import send_mail

from students.models import Logger


@shared_task
def send_email_async(subject, message, email_from, recipient_list):
    send_mail(subject, message, email_from, recipient_list)


@task
def clean_old_logs(days):
    now = datetime.now(timezone.utc)
    Logger.objects.filter(created__lte=now - timedelta(days=days)).delete()
    # queryset = Logger.objects.all()
    # for q in queryset:
    #     print(q.created)
    # print(f'Method for cleaning data older then {days} days.')
