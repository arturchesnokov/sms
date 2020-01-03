from datetime import datetime
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
        return f'{self.first_name} {self.last_name} {self.birth_date}'

    @classmethod
    def generate_student(cls):
        fake = Faker('en_US')
        fake.add_provider(phone_number)
        fake.add_provider(profile)
        f_profile = fake.profile()
        f_names = f_profile['name'].split(' ')
        student = cls(
            first_name=f_names[0],
            last_name=f_names[1],
            birth_date=f_profile['birthdate'],
            email=f_profile['mail'],
            telephone=fake.phone_number(),
            address=f_profile['address']
        )
        student.save()
        return f"First Name: {student.first_name}" \
               f"<br />Last Name: {student.last_name}" \
               f"<br />Birth date: {student.birth_date}" \
               f"<br />Email: {student.email}" \
               f"<br />Phone: {student.telephone}" \
               f"<br />Address: {student.address}"


class Group(models.Model):
    group_name = models.CharField(max_length=50)
    start_date = models.DateField()
    students_count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)

    def get_info(self):
        return f'{self.group_name} {self.students_count} {self.is_active}'
