from django.forms import ModelForm, Form, EmailField, CharField, ValidationError
from django.core.mail import send_mail
from django.conf import settings

from students.models import Student, Group


class StudentsAddForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentAdminForm(ModelForm):
    class Meta:
        model = Student
        fields = ('id', 'email', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if Student.objects.filter(email__iexact=email).exists():
            raise ValidationError(f'{email} already used!')
        return email


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
