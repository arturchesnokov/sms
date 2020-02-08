import time

from students.models import Logger
from students.tasks import logger_write_db


class LoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        full_time = time.time() - start_time

        full_path = request.path

        # print('--------------')
        # print(request)
        # print(response)
        # print('fullpath', full_path)
        # print('id:', request.user.pk)
        # print('--------------')

        if full_path.startswith('/admin/'):
            if request.user.pk is None:  # TODO  как избежать вот такого?
                request.user.pk = 0

            logger_write_db.delay(full_path, request.method, full_time, int(request.user.pk))

        return response
