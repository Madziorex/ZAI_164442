from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    tmdb_id = models.IntegerField(unique=True)
    poster_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title