from core.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class LoginTestCase(APITestCase):
    def test_login(self):
        # Create a test user
        username = 'testusername'
        password = 'testpassword'
        email = 'email@example.com'
        user = User.objects.create(username=username, email=email, password=password)

        #user.save()

        # Prepare the login data
        login_data = {
            'username': username,
            'password': password
        }

        url = reverse('login')
        response = self.client.post(url, login_data, format='json')

        print(response.data)

        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        self.assertIn('message', response.data)
        self.assertEqual(response.data['message'], 'Login success')

        # Verify the session cookie
        self.assertTrue('token' in self.client.cookies)

        # Verify the generated token
        token = response.data['token']
        self.assertEqual(user.auth_token.key, token)
