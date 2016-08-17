from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Movie(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    description = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    @property
    def avg_rating(self):
        return Rating.objects.filter(movie__id=self.id).aggregate(models.Avg('stars'))


class Rating(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    movie = models.ForeignKey(Movie)
    user = models.ForeignKey(User)
    stars = models.IntegerField(choices=RATING_CHOICES)
    pub_date = models.DateTimeField(auto_now_add=True)

