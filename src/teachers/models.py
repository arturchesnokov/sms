from django.db import models

from faker import Faker
from faker.providers import phone_number, profile


class Teacher(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    birth_date = models.DateField()
    email = models.EmailField(unique=True)
    # add avatar TODO
    telephone = models.CharField(unique=True, max_length=25)
    address = models.CharField(max_length=255, null=True, blank=True)

    def get_info(self):
        return f"First Name: {self.first_name}" \
               f"<br />Last Name: {self.last_name}" \
               f"<br />Birth date: {self.birth_date}" \
               f"<br />Email: {self.email}" \
               f"<br />Phone: {self.telephone}" \
               f"<br />Address: {self.address}"

    @classmethod
    def generate_teacher(cls):
        fake = Faker('en_US')
        fake.add_provider(phone_number)
        fake.add_provider(profile)
        f_profile = fake.profile()
        teacher = cls(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            birth_date=f_profile['birthdate'],
            email=fake.email(),
            telephone=fake.phone_number(),
            address=fake.address()
        )
        teacher.save()
        return teacher

    def __str__(self):
        return f'{self.id} - {self.full_name}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
