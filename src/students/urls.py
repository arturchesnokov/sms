from django.contrib import admin
from django.urls import path

from students.views import (students, generate_student, students_add, students_edit,
                            groups, generate_group, groups_add, groups_edit,
                            contact)

urlpatterns = [
    path('gen/', generate_student, name='students-generate'),
    path('list/', students, name='students'),
    path('add/', students_add, name='students-add'),
    path('edit/<int:pk>/', students_edit, name='students-edit'),

    path('contact/', contact, name='contact'),

    path('groups/', groups, name='groups'),
    path('groups/add/', groups_add, name='groups-add'),
    path('generate-group/', generate_group, name='groups-generate'),
    path('groups-edit/<int:pk>/', groups_edit, name='groups-edit'),

]
