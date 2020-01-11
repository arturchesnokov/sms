from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Teacher
from teachers.forms import TeachersAddForm


def generate_teacher(request):
    teacher = Teacher.generate_teacher()
    return HttpResponse(teacher.get_info())


def teachers(request):
    queryset = Teacher.objects.all()
    response = ''

    f_name = request.GET.get('first_name')
    if f_name:
        queryset = queryset.filter(first_name__startswith=f_name)

    print(queryset.query)

    for teacher in queryset:
        response += teacher.get_info() + '<br><br>'
    return render(request,
                  'teachers_list.html',
                  context={'teachers_list': response})


def add_teacher(request):
    if request.method == 'POST':
        form = TeachersAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')
    else:
        form = TeachersAddForm()
    return render(request,
                  'add_teacher.html',
                  context={'form': form})
