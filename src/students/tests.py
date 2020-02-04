from django.test import TestCase
from django.test import Client
from django.urls import reverse
from faker import Faker

from students.models import Student


class TestContact(TestCase):
    fake = Faker()

    def test_form(self):
        data = {
            'email': self.fake.email(),
            'subject': self.fake.word(),
            'text': self.fake.text()
        }
        response = self.client.post(reverse('contact'), data)
        assert response.status_code == 302

        data['email'] = 'WRONG'
        response = self.client.post(reverse('contact'), data)
        assert response.status_code == 200


class TestReg(TestCase):
    def test_reg_form(self):
        test_email = f'test+123@mail.com'
        data = {
            'email': test_email,
        }
        response = self.client.post(reverse('reg-form'), data)
        assert response.status_code == 302  # form check

        student = Student.objects.get(email=test_email)

        assert student.email == test_email  # student has been created

        assert student.is_enabled == False  # default status of created student

        response = self.client.get(reverse('students-confirm', args=[student.pk]))
        # student = Student.objects.get(email=test_email)
        student.refresh_from_db()
        assert student.is_enabled is True


class StudentListTestResponse(TestCase):
    fixtures = ['db.json']

    def test_response_code(self):
        client = Client()
        response = client.get(reverse('students'))
        self.assertEqual(response.status_code, 200, msg='students page response status - FAIL')

        students_list = response.context['students']
        #print('students_list', response.context['students'])

        qs_students = Student.objects.all()
        # print(f'QS: {qs_students}')
        self.assertQuerysetEqual(qs_students.order_by('id'), map(str, students_list.order_by('id')), transform=str)


class StudentAddPageTestResponse(TestCase):

    def test_response_code(self):
        client = Client()
        response = client.get(reverse('students-add'), msg='student Add page response status - FAIL')
        self.assertEqual(response.status_code, 200)


class StudentCreate(TestCase):

    def setUp(self):
        st = Student(first_name='First',
                     last_name='Last',
                     birth_date='1990-11-11',
                     email='email@gmail.com',
                     telephone='0123456789',
                     address='Some test address, 12345',
                     group=None)
        st.save()

    def test_student_info(self):
        student = Student.objects.get(first_name='First')
        self.assertEqual(student.first_name, 'First')
        self.assertEqual(student.last_name, 'Last')

    def test_student_edit(self):
        student = Student.objects.get(first_name='First')
        student.last_name = 'Jason'
        student.save()

        s = Student.objects.get(first_name='First')
        self.assertEqual(s.last_name, 'Jason')
