import time

from students.models import Logger


class LoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)
        full_path = request.build_absolute_uri()

        # print('--------------')
        # print(request)
        # print(response)
        # print('fullpath', full_path)
        # print('id:', request.user.pk)
        # print('--------------')

        end_time = time.time()
        full_time = end_time - start_time

        if '/admin/' in full_path:
            if request.user.pk is None:  # TODO  как избежать вот такого?
                request.user.pk = 0
            Logger.objects.create(path=full_path,
                                  method=request.method,
                                  time_delta=full_time,
                                  user_id=int(request.user.pk))

        return response
