from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class RegisterTest(APITestCase):
    def register_user(self):
        """
        create a new user.
        """
        url = reverse('register')
        data = {"username": "testuser", "email": "test@email.com",
                "password": "testpass"}
        return self.client.post(url, data, format='json')

    def test_register_user(self):
        response = self.register_user()
        self.assertEqual(response.data, {"username": "testuser",
                                         "email": "test@email.com"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_token(self):
        self.register_user()
        data = {"username": "testuser", "password": "testpass"}
        response = self.client.post('/api-token-auth/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_duplicate_user(self):
        """
        create a duplicate user.
        """
        self.register_user()
        response = self.register_user()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
