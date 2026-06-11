import requests
import httpx
from django.conf import settings
from .models import Movie

TMDB_URL = "https://api.themoviedb.org/3/movie/popular"

async def fetch_movies_async():
    params = {
        "api_key": settings.TMDB_API_KEY,
        "language": "en-US",
        "page": 1
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(TMDB_URL, params=params)

    if response.status_code != 200:
        raise Exception("Błąd pobierania danych z TMDB")

    data = response.json()
    return data["results"]

def save_movies(movies_data):
    for movie in movies_data:
        Movie.objects.update_or_create(
            tmdb_id=movie["id"],
            defaults={
                "title": movie["title"],
                "description": movie["overview"],
                "release_date": movie.get("release_date") or None,
                "rating": movie.get("vote_average"),
                "poster_url": f"https://image.tmdb.org/t/p/w500{movie.get('poster_path')}"
                if movie.get("poster_path") else None,
            }
        )