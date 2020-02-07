from celery import shared_task, task
from time import sleep

from django.core.mail import send_mail


@shared_task
def send_email_async(subject, message, email_from, recipient_list):
    send_mail(subject, message, email_from, recipient_list)


@task
def clean_old_data(days):
    print(f'Here must be method to clean data for {days} days.')
