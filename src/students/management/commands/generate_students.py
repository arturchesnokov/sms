import random

from django.core.management.base import BaseCommand

from students.models import Student, Group
from teachers.models import Teacher


class Command(BaseCommand):
    help = 'Creates 100 fake students'

    def handle(self, *args, **options):
        Group.objects.all().delete()
        Student.objects.all().delete()
        Teacher.objects.all().delete()

        groups = []
        teachers = []
        students = []

        for _ in range(10):
            teachers.append(Teacher.generate_teacher())
            groups.append(Group.generate_group())

        for _ in range(100):
            student = Student.generate_student()
            student.group = random.choice(groups)
            students.append(student)
            student.save()

        for group in groups:
            group.curator = random.choice(teachers)
            group.praepostor = random.choice(students)
            group.save()
