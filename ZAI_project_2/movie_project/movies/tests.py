from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Movie
from django.contrib.auth.models import User


class MovieAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test123')
        self.client.login(username='test', password='test123')
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="Test desc",
            rating=7.5,
            tmdb_id=123
        )

    def test_get_movies_list(self):
        url = reverse('movie-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_create_movie(self):
        url = reverse('movie-list')
        data = {
            "title": "New Movie",
            "description": "desc",
            "rating": 8.0,
            "tmdb_id": 999
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)