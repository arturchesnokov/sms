from django.core.management.base import BaseCommand

from students.models import Student


class Command(BaseCommand):
    help = 'Generate random students'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            help='Delete poll instead of closing it',
        )

    def handle(self, *args, **options):
        number = int(options.get('number') or 100)
        for _ in range(number):
            Student.generate_student()



