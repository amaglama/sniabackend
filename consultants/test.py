# tests.py
from rest_framework.test import APITestCase
from rest_framework import status

class RegisterAPITest(APITestCase):
    def test_register_success(self):
        url = '/register/'
        data = {
            "email": "test@example.com",
            "name": "Test User",
            "category": "A"
        }
        response = self.client.post(url, data, format='json')
        
        # Assert response status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Assert response content
        self.assertEqual(response.data['message'], "Registration successful! Email sent.")
