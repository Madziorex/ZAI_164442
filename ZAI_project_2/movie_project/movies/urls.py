from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, import_movies

router = DefaultRouter()
router.register(r'movies', MovieViewSet)

urlpatterns = [
    path('import-movies/', import_movies),
    path('', include(router.urls)),
]