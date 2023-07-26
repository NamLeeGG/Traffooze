from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from core.models import User

class RegisterAccountTestCase(APITestCase):
    def test_register_account(self):
        # Prepare the registration data
        registration_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@example.com',
        }

        # Send a POST request to the register_account endpoint
        url = reverse('register')
        response = self.client.post(url, registration_data)

        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify that the user is created
        user = User.objects.get(username=registration_data['username'])
        self.assertEqual(user.email, registration_data['email'])
        self.assertTrue(user.check_password(registration_data['password']))

        print("test register passed")

    def test_register_account_empty_password(self):
        # Prepare the registration data with an empty password
        registration_data = {
            'username': 'testuser',
            'password': '',
            'email': 'test@example.com',
        }

        # Send a POST request to the register_account endpoint
        url = reverse('register')
        response = self.client.post(url, registration_data)

        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['error'], 'Password cannot be empty'
        )

        print("test register empty password passed")


'''
import json
from core.models import User
from django.db import DatabaseError
from django.test import TestCase, Client

class RegisterAccountTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.valid_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@example.com'
        }
    
    def test_register_account_success(self):
        response = self.client.post('register', data=self.valid_data)
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, None)  # No response data expected
        
        # Perform additional assertions to ensure the user is created correctly
        user = User.objects.get(username=self.valid_data['username'])
        self.assertEqual(user.email, self.valid_data['email'])
        self.assertTrue(user.check_password(self.valid_data['password']))
'''
    
'''
    def test_register_account_empty_password(self):
        invalid_data = self.valid_data.copy()
        invalid_data['password'] = ''  # Empty password
        response = self.client.post('/register_account/', data=invalid_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data['error'], 'Password cannot be empty'
        )
    
'''
'''
    def test_register_account_database_error(self):
        # Simulate a database error by forcing an exception
        with self.assertRaises(DatabaseError):
            with patch('path.to.register_account.User.save') as mock_save:
                mock_save.side_effect = DatabaseError()
                response = self.client.post('/register_account/', data=self.valid_data)
                self.assertEqual(response.status_code, 500)
                self.assertEqual(
                    response.data['error'], 'Bad data'
                )
'''