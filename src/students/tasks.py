from celery import shared_task, task
from datetime import datetime, timedelta, timezone

from django.core.mail import send_mail

from students.models import Logger


@shared_task
def send_email_async(subject, message, email_from, recipient_list):
    send_mail(subject, message, email_from, recipient_list)

@shared_task
def logger_write_db(path, method, time, user_id):
    Logger.objects.create(path=path,
                          method=method,
                          time_delta=time,
                          user_id=user_id)


@task
def clean_old_logs(days):
    now = datetime.now(timezone.utc)
    Logger.objects.filter(created__lte=now - timedelta(days=days)).delete()
    # queryset = Logger.objects.all()
    # for q in queryset:
    #     print(q.created)
    # print(f'Method for cleaning data older then {days} days.')
