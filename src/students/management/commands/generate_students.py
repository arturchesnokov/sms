import random

from django.core.management.base import BaseCommand

from students.models import Student, Group


class Command(BaseCommand):
    help = 'Creates 100 fake students'

    def handle(self, *args, **options):
        Group.objects.all().delete()
        Student.objects.all().delete()
        groups = []

        for _ in range(10):
            groups.append(Group.generate_group())

        for _ in range(100):
            student = Student.generate_student()
            student.group = random.choice(groups)
            student.save()
