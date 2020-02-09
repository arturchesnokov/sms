from django.forms import ModelForm, ValidationError

from teachers.models import Teacher


class BaseTeacherForm(ModelForm):

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        email_exists = Teacher.objects. \
            filter(email__iexact=email). \
            exclude(id=self.instance.id). \
            exists()
        if email_exists:
            raise ValidationError(f'Email {email} is already used')
        return email


class TeachersAddForm(BaseTeacherForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherAdminForm(BaseTeacherForm):
    class Meta:
        model = Teacher
        fields = '__all__'
