from faker import Faker
from faker.providers import phone_number, profile

from django.db import models

'''
CREATE TABLE students_student(
first_name varchar(20)
last_name varchar(20)
birth_date
email
phone
'''


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    email = models.EmailField()
    # add avatar TODO
    telephone = models.CharField(max_length=16)  # clean phone TODO
    address = models.CharField(max_length=255, null=True, blank=True)

    def get_info(self):
        return f"First Name: {self.first_name}" \
               f"<br />Last Name: {self.last_name}" \
               f"<br />Birth date: {self.birth_date}" \
               f"<br />Email: {self.email}" \
               f"<br />Phone: {self.telephone}" \
               f"<br />Address: {self.address}"

    @classmethod
    def generate_student(cls):
        fake = Faker('en_US')
        fake.add_provider(phone_number)
        fake.add_provider(profile)
        f_profile = fake.profile()
        student = cls(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            birth_date=f_profile['birthdate'],
            email=fake.email(),
            telephone=fake.phone_number(),
            address=fake.address()
        )
        student.save()
        return student


class Group(models.Model):
    group_name = models.CharField(max_length=50)
    start_date = models.DateField()
    students_count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)

    def get_info(self):
        return f'<br>Group:{self.group_name} ' \
               f'<br>Students count:{self.students_count} ' \
               f'<br>is Activ:{self.is_active}' \
               f'<br>Start date:{self.start_date}'

    @classmethod
    def generate_group(cls):
        fake = Faker('en_US')
        group = cls(
            group_name=fake.bothify(text="??##", letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
            start_date=fake.date_between(start_date="-1y", end_date="today"),
            students_count=fake.random_int(min=1, max=20, step=1),
            is_active=fake.boolean(chance_of_getting_true=70)
        )
        group.save()
        return group
