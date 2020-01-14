from django.contrib import admin
from django.urls import path

from students.views import (generate_student, students, generate_group, groups,
                            students_add, add_group, students_edit, contact)

urlpatterns = [
    path('gen/', generate_student),
    path('list/', students, name='students'),
    path('add/', students_add, name='students-add'),
    path('edit/<int:pk>/', students_edit, name='students-edit'),

    path('contact/', contact, name='contact'),

    path('groups/', groups),
    path('groups/add/', add_group),
    path('generate-group/', generate_group),

]
