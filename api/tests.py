from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, force_authenticate


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


class MovieTest(APITestCase):
    def register_user(self):
        """
        create a new user.
        """
        url = reverse('register')
        data = {"username": "testuser", "email": "test@email.com",
                "password": "testpass"}
        return self.client.post(url, data, format='json')

    def test_add_movie(self):
        """
        create a new movie.
        """
        self.register_user()
        user = User.objects.get(username='testuser')
        token = Token.objects.get(user=user)
        url = reverse('movies')
        data = {"title": "movie title", "description": "this is description"}
        response = self.client.post(url, data, format='json',
                                    HTTP_AUTHORIZATION='Token {}'.format(token))
        print response
        self.assertEqual(response.data, {"title": "movie title",
                                         "description": "this is description"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
