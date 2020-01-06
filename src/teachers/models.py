from django.db import models

from faker import Faker
from faker.providers import phone_number, profile

from django.db import models


class Teacher(models.Model):
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
