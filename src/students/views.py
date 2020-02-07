from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse

from .models import Student, Group, Logger
from students.forms import StudentsAddForm, GroupsAddForm, ContactForm, RegForm, StudentsEditForm


# Student methods
def generate_student(request):
    student = Student.generate_student()
    return HttpResponse(student.get_info())


def students(request):
    queryset = Student.objects.all().select_related('group')

    name = request.GET.get('first_name')
    if name:
        queryset = queryset.filter(Q(first_name__contains=name) |
                                   Q(last_name__contains=name) |
                                   Q(email__contains=name))
    return render(request,
                  'students_list.html',
                  context={'students': queryset})


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
    queryset = Group.objects.all().select_related('praepostor', 'curator')

    g_name = request.GET.get('g_name')
    if g_name:
        # __contains -> LIKE %{}%
        queryset = queryset.filter(group_name__contains=g_name)

    return render(request,
                  'groups_list.html',
                  context={'groups': queryset})


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


# Reg form methods
def reg_form(request):
    if request.method == 'POST':
        form = RegForm(request.POST, request=request)  # обрабатываем данные
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = RegForm()  # отображаем форму

    return render(request, 'reg.html', context={'form': form})


def students_confirm(request, pk):
    # get_object_or_404
    try:
        student = Student.objects.get(id=pk)
        student.is_enabled = True  # change the status
        student.save()
    except Student.DoesNotExist:
        return HttpResponseNotFound(f'Student with id {pk} not found')

    if request.method == 'POST':
        form = StudentsEditForm(request.POST, instance=student)  # обрабатываем данные
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentsEditForm(instance=student)  # отображаем форму

    return render(request, 'students_confirm.html', context={'form': form, 'pk': pk})


def admin_logger(request):
    queryset = Logger.objects.all()
    return render(request, 'admin_logger_template.html', context={'admin_logger': queryset})
