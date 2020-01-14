from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse

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


def teachers_add(request):
    if request.method == 'POST':
        form = TeachersAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers'))
    else:
        form = TeachersAddForm()
    return render(request,
                  'teachers_add.html',
                  context={'form': form})


def teachers_edit(request, pk):
    try:
        teacher = Teacher.objects.get(id=pk)
    except Teacher.DoesNotExist:
        return HttpResponseNotFound(f'Teacher with id {pk} not found')

    if request.method == 'POST':
        form = TeachersAddForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers'))
    else:
        form = TeachersAddForm(instance=teacher)

    return render(request, 'teachers_edit.html', context={'form': form, 'pk': pk})
