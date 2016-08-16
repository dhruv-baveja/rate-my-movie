from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Movie(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    description = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
