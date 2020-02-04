from celery import shared_task
from time import sleep

from django.core.mail import send_mail


@shared_task
def add(a, b):
    print('ADD WORKS')
    sleep(10)
    print(a + b)
    return a + b


@shared_task
def send_email_async(subject, message, email_from, recipient_list):
    send_mail(subject, message, email_from, recipient_list)
