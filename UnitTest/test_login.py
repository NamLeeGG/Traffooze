from core.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from api.checklist import *

class LoginTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.username = 'testusername'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password, email="email@example.com")

    def test_login(self):
        if not login_exists:
            return
        
        url = reverse('login')

        data = {'username': self.username, 'password': self.password}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        self.assertIn('message', response.data)
        self.assertEqual(response.data['message'], 'Login success')
        self.assertTrue('token' in self.client.cookies)
        token = response.data['token']
        self.assertEqual(self.user.auth_token.key, token)

        print("test login passed")

    #Login fail
    def test_login_invalid(self):
        if not login_exists:
            return
        
        url = reverse('login')

        data = {'username': 'invalidusername', 'password': self.password}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIn('Invalid credentials', response.data['detail'])
        self.assertNotIn('token', response.data)
        self.assertNotIn('token', response.cookies)

        print("test login invalid credentials passed")

    def addFailure(self, test, exc_info):
        super().addFailure(test, exc_info)
        print(f"Unit test '{test.__name__}' failed: {exc_info[1]}")

    def tearDown(self):
        self.user.delete()