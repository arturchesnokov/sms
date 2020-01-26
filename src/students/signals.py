from django.db.models.signals import pre_save
from django.dispatch import receiver
from students.models import Student


@receiver(pre_save, sender=Student)
def pre_save_student(sender, instance, **kwargs):
    instance.email = instance.email.lower()
