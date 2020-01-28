from django.test import TestCase, SimpleTestCase
import unittest
from django.test import Client
from django.urls import reverse


class StudentListTest(TestCase):

    def test_response_code(self):
        client = Client()
        response = client.get(reverse('students'))
        self.assertEqual(response.status_code, 200)
