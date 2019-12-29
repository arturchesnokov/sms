from datetime import datetime

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
        student = cls(
            first_name='D',
            last_name='K',
            birth_date=datetime.now().date(),
            email = 'erwerwerf@gmail.com',
            telephone = '234234234',
        )
        student.save()
