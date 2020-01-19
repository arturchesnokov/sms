import random

from faker import Faker
from faker.providers import phone_number, profile

from django.db import models

from teachers.models import Teacher


class Student(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    birth_date = models.DateField()
    email = models.EmailField()
    # add avatar TODO
    telephone = models.CharField(max_length=25)  # clean phone TODO
    address = models.CharField(max_length=255, null=True, blank=True)
    group = models.ForeignKey('students.Group',
                              null=True, blank=True,
                              on_delete=models.CASCADE)

    def get_info(self):
        return f"First Name: {self.first_name}" \
               f"<br />Last Name: {self.last_name}" \
               f"<br />Birth date: {self.birth_date}" \
               f"<br />Email: {self.email}" \
               f"<br />Phone: {self.telephone}" \
               f"<br />Address: {self.address}" \
               #f"<br />Group: {self.group.group_name}"

    @classmethod
    def generate_student(cls):
        fake = Faker('en_US')
        fake.add_provider(phone_number)
        fake.add_provider(profile)
        f_profile = fake.profile()
        #groups_list = list(Group.objects.all())
        student = cls(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            birth_date=f_profile['birthdate'],
            email=fake.email(),
            telephone=fake.phone_number(),
            address=fake.address(),
            #group=random.choice(groups_list)
        )
        student.save()
        return student

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Group(models.Model):
    group_name = models.CharField(max_length=50)
    start_date = models.DateField()
    students_count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    praepostor = models.ForeignKey(Student,
                                   related_name='head_of_group',
                                   null=True, blank=True,
                                   on_delete=models.CASCADE)

    curator = models.ForeignKey(Teacher,
                                null=True, blank=True,
                                on_delete=models.CASCADE)

    def get_info(self):
        return f'<br>Group:{self.group_name} ' \
               f'<br>Students count:{self.students_count} ' \
               f'<br>is Activ:{self.is_active}' \
               f'<br>Start date:{self.start_date}' \
               f'<br>Curator:{self.curator} ' \
               f'<br>Praepostor:{self.praepostor} '

    @classmethod
    def generate_group(cls):
        fake = Faker('en_US')
        #teachers = list(Teacher.objects.all())
        #students = list(Student.objects.all())
        group = cls(
            group_name=fake.bothify(text="??##", letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
            start_date=fake.date_between(start_date="-1y", end_date="today"),
            students_count=fake.random_int(min=1, max=20, step=1),
            is_active=fake.boolean(chance_of_getting_true=70),
            #praepostor=random.choice(students),
            #curator=random.choice(teachers)
        )
        group.save()
        return group

    def __str__(self):
        return self.group_name
