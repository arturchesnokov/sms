from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse

from .models import Student, Group
from students.forms import StudentsAddForm, GroupsAddForm, ContactForm


# Student methods
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
        response += f'<a href="{reverse("students-edit", args=[student.pk])}">' + student.get_info() + '</a><br><br>'
    return render(request,
                  'students_list.html',
                  context={'students_list': response})


def students_add(request):
    if request.method == 'POST':
        form = StudentsAddForm(request.POST)  # обрабатываем данные
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentsAddForm()  # отображаем форму

    return render(request, 'students_add.html', context={'form': form})


def students_edit(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return HttpResponseNotFound(f'Student with id {pk} not found')

    if request.method == 'POST':
        form = StudentsAddForm(request.POST, instance=student)  # обрабатываем данные
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentsAddForm(instance=student)  # отображаем форму

    return render(request, 'students_edit.html', context={'form': form, 'pk': pk})


# Group methods
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
    print(queryset.query)

    for group in queryset:
        response += group.get_info_as_link(f'<a href="{reverse("groups-edit", args=[group.pk])}">') + '<br>'
    return render(request,
                  'groups_list.html',
                  context={'groups_list': response})


def groups_add(request):
    if request.method == 'POST':
        form = GroupsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups'))
    else:
        form = GroupsAddForm()
    return render(request,
                  'groups_add.html',
                  context={'form': form})


def groups_edit(request, pk):
    try:
        group = Group.objects.get(id=pk)
    except Group.DoesNotExist:
        return HttpResponseNotFound(f'Group with id {pk} not found')

    if request.method == 'POST':
        form = GroupsAddForm(request.POST, instance=group)  # обрабатываем данные
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups'))
    else:
        form = GroupsAddForm(instance=group)  # отображаем форму

    return render(request, 'groups_edit.html', context={'form': form, 'pk': pk})


# Contact form methods
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  # обрабатываем данные
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = ContactForm()  # отображаем форму

    return render(request, 'contact.html', context={'form': form})
