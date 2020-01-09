from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q

from .models import Student, Group
from students.forms import StudentsAddForm


def generate_student(request):
    student = Student.generate_student()
    return HttpResponse(student.get_info())


def students(request):
    queryset = Student.objects.all()
    response = ''

    name = request.GET.get('first_name')
    if name:
        queryset = queryset.filter(Q(first_name__contains=name) |
                                   Q(last_name__contains=name) |
                                   Q(email__contains=name))

        # __contains -> LIKE %{}%
        # queryset = queryset.filter(first_name__contains=f_name)
        # __endswith -> LIKE {}%
        # queryset = queryset.filter(first_name__endswith=f_name)
        # __startswith -> LIKE %{}
        # queryset = queryset.filter(first_name__startswith=f_name)

    print(queryset.query)

    for student in queryset:
        response += student.get_info() + '<br><br>'
    return render(request,
                  'students_list.html',
                  context={'students_list': response})


def generate_group(request):
    group = Group.generate_group()
    return HttpResponse(group.get_info())


def groups(request):
    queryset = Group.objects.all()
    response = ''

    g_name = request.GET.get('g_name')
    if g_name:
        # __contains -> LIKE %{}%
        queryset = queryset.filter(group_name__contains=g_name)
        # __endswith -> LIKE {}%
        # queryset = queryset.filter(first_name__endswith=f_name)
        # __startswith -> LIKE %{}
        # queryset = queryset.filter(first_name__startswith=f_name)

    print(queryset.query)

    for group in queryset:
        response += group.get_info() + '<br>'
    return render(request,
                  'groups_list.html',
                  context={'groups_list': response})


def add_student(request):
    if request.method == 'POST':
        form = StudentsAddForm(request.POST)  # обрабатываем данные
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')
    else:
        form = StudentsAddForm()  # отображаем форму

    return render(request,
                  'add_student.html',
                  context={'form': form})
