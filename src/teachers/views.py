from django.http import HttpResponse
from django.shortcuts import render

from .models import Teacher


def generate_teacher(request):
    teacher = Teacher.generate_teacher()
    return HttpResponse(teacher.get_info())


def teachers(request):
    queryset = Teacher.objects.all()
    response = ''

    f_name = request.GET.get('first_name')
    if f_name:
    # __contains -> LIKE %{}%
        #queryset = queryset.filter(first_name__contains=f_name)
    # __endswith -> LIKE {}%
        #queryset = queryset.filter(first_name__endswith=f_name)
    # __startswith -> LIKE %{}
        queryset = queryset.filter(first_name__startswith=f_name)

    print(queryset.query)

    for teacher in queryset:
        response += teacher.get_info() + '<br><br>'
    return render(request,
                  'teachers_list.html',
                  context={'teachers_list': response})