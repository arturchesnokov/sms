from django.urls import path

from teachers.views import teachers, teachers_add, generate_teacher, teachers_edit

# root of app -> /teachers/
urlpatterns = [
    path('', teachers, name='teachers'),
    path('add/', teachers_add, name='teachers-add'),
    path('gen/', generate_teacher, name='teachers-generate'),
    path('edit/<int:pk>/', teachers_edit, name='teachers-edit'),

]
