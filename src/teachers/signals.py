from django.db.models.signals import pre_save
from django.dispatch import receiver
from teachers.models import Teacher


def only_numbers(st):
    return ''.join([n for n in st if n.isdigit()])


@receiver(pre_save, sender=Teacher)
def pre_save_teacher(sender, instance, **kwargs):
    instance.email = instance.email.lower()
    instance.first_name = instance.first_name.strip().lower().capitalize()
    instance.last_name = instance.last_name.strip().lower().capitalize()
    instance.telephone = only_numbers(instance.telephone)
