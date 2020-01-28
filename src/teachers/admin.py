from django.contrib import admin

from teachers.models import Teacher
from teachers.forms import TeacherAdminForm


class TeachersAdmin(admin.ModelAdmin):
    # readonly_fields = ('email', 'telephone')
    list_display = ('id', 'first_name', 'last_name', 'email')
    list_per_page = 10
    form = TeacherAdminForm


admin.site.register(Teacher, TeachersAdmin)
