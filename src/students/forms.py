from django.forms import ModelForm, Form, EmailField, CharField, ValidationError
from django.core.mail import send_mail
from django.conf import settings

from students.models import Student, Group


class BaseStudentForm(ModelForm):

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        email_exists = Student.objects. \
            filter(email__iexact=email). \
            exclude(id=self.instance.id). \
            exists()
        if email_exists:
            raise ValidationError(f'Email {email} is already used')
        return email


class StudentsAddForm(BaseStudentForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentAdminForm(BaseStudentForm):
    class Meta:
        model = Student
        # fields = '__all__'
        fields = ('id', 'email', 'first_name', 'last_name', 'telephone')


class GroupsAddForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'


class ContactForm(Form):
    email = EmailField()
    subject = CharField()
    text = CharField()

    def save(self):
        data = self.cleaned_data  # validated data
        subject = data['subject']
        message = data['text']
        email_from = data['email']
        recipient_list = [settings.EMAIL_HOST_USER]

        send_mail(subject, message, email_from, recipient_list)

        with open('mail_log.txt', 'a') as mail_log:
            mail_log.write(f'Email: {email_from}\n'
                           f'Subject: {subject}\n'
                           f'Message: {message}\n\n')
            mail_log.close()
