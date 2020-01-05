from django.core.management.base import BaseCommand

from students.models import Student


class Command(BaseCommand):
    help = 'Creates 100 fake students'

    def add_arguments(self, parser):
        parser.add_arguments(
            '--number',
            help='Creates 100 fake students',
        )

    def handle(self, *args, **options):
        # from pdb import set_trace
        # set_trace()
        number = int(options.get('numbers') or 100)
        for _ in range(number):
            Student.generate_student()



