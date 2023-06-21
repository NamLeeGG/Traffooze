from core.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from unittest.mock import patch
#from django.http import HttpRequest

class LogoutTestCase(APITestCase):
    @patch('api.views.logout')
    def test_logout(self, mock_logout):
        # Create a user and obtain an authentication token
        user = User.objects.create(username='testusername')
        token = Token.objects.create(user=user)

        # Set the authentication token in the test client's headers
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        # Send a POST request to the logout endpoint
        url = reverse('logout')
        #request = self.client.post(url).wsgi_request
        response = self.client.post(url)

        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Logout success')

        # Check that the token is deleted
        self.assertFalse(Token.objects.filter(user=user).exists())

        # Check that the token cookie is deleted
        self.assertEqual(response.cookies.get('token').value, '')

        #mock_logout.assert_called_once_with(request)

        print("test logout passed")

''''
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from core.models import User
from rest_framework import status


class LogoutViewTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass', email='testemail@gmail.com')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_logout(self):
        response = self.client.post('/logout/')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Token.objects.filter(user=self.user).exists())
        self.assertNotIn('token', response.cookies)
        self.assertEqual(response.data, {'message': 'Logout success'})
        print("\nUnit test Logout_1 passed")

    def test_logout_not_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.post('/logout/')
        #print(response.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        print("\nUnit test Logout_2 passed")
'''