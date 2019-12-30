from django.core.management.base import BaseCommand

from students.models import Student


class Command(BaseCommand):
    help = 'Creates 100 fake students'

    def handle(self, *args, **options):
        for i in range(100):
            Student.generate_student()

