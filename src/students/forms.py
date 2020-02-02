from django.forms import ModelForm, Form, EmailField, CharField, ValidationError
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.http import request

from students.models import Student, Group
from students.tasks import send_email_async

import random


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


class StudentsEditForm(BaseStudentForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'email',
                  'telephone', 'birth_date', 'address', 'group', 'password')
        read_only_fields = ('is_enabled', 'username')  # TODO show fields in RO mode


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

        # student = Student.objects.get_or_create(email = email_from)[0]

        send_email_async.delay(subject, message, email_from, recipient_list)

        with open('mail_log.txt', 'a') as mail_log:
            mail_log.write(f'Email: {email_from}\n'
                           f'Subject: {subject}\n'
                           f'Message: {message}\n\n')


class RegForm(Form):
    email = EmailField()

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def save(self):
        data = self.cleaned_data  # validated data
        subject = 'Registration confirmation'
        email_from = data['email']
        recipient_list = [settings.EMAIL_HOST_USER]

        # TODO rewrite to use get_or_create()
        try:
            student = Student.objects.get(email=email_from)
        except:
            student = Student(
                email=email_from,
                username=email_from[:email_from.find('@')],
                telephone=str(random.randrange(1000000, 9999999)),
                birth_date='1980-01-01',
            )
            import uuid
            str(uuid.uuid4())

        student.save()
        full_path = self.request.build_absolute_uri(reverse('students-confirm', args=[2]))
        message = 'Hello, you need to finish account registration,\n' \
                  'please follow the link to confirm your email:\n' \
                  f'{full_path}\n'

        # TODO insert absolute url, not hardcode
        # f'{request.build_absolute_uri(reverse("students-edit", args=[student.pk]))}'

        send_email_async.delay(subject, message, email_from, recipient_list)

        with open('mail_log.txt', 'a') as mail_log:
            mail_log.write(f'Email: {email_from}\n'
                           f'Subject: {subject}\n'
                           f'Message: {message}\n\n')
