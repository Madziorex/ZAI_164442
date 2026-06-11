from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, filters
from .models import Movie
from .serializers import MovieSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from .services import fetch_movies_async, save_movies
import asyncio

@api_view(['POST'])
def import_movies(request):
    movies = asyncio.run(fetch_movies_async())
    save_movies(movies)

    return Response({"message": "Filmy zaimportowane!"})

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['release_date', 'rating']
    search_fields = ['title', 'description']
    ordering_fields = ['rating', 'release_date', 'id']