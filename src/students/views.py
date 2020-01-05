from django.http import HttpResponse
from django.shortcuts import render

from .models import Student


def generate_student(request):
    student = Student.generate_student()
    return HttpResponse(student.get_info())


def students(request):
    queryset = Student.objects.all()
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

    for student in queryset:
        response += student.get_info() + '<br><br>'
    return render(request,
                  'students_list.html',
                  context={'students_list': response})
