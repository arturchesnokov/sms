from django.contrib import admin

from students.forms import StudentAdminForm
from students.models import Student, Group


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'group')
    list_select_related = ('group',)
    list_per_page = 10
    form = StudentAdminForm

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='manager').exists():
            return ('email', 'telephone')
        return ()


class StudentInline(admin.TabularInline):
    model = Student
    fields = ('first_name', 'last_name', 'email', 'telephone', 'address')
    readonly_fields = ('first_name', 'last_name', 'birth_date', 'email', 'telephone', 'address', 'group')
    # show_change_link = True


class GroupAdmin(admin.ModelAdmin):
    # readonly_fields = ('email', 'telephone')
    list_display = ('id', 'group_name', 'is_active', 'start_date', 'curator', 'praepostor')
    list_select_related = ('curator', 'praepostor')
    list_per_page = 10
    inlines = [StudentInline, ]


admin.site.register(Student, StudentAdmin)

admin.site.register(Group, GroupAdmin)
