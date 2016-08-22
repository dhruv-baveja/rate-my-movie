from celery.task.schedules import crontab
from celery.decorators import periodic_task

from django.conf import settings
from django.core.mail import send_mail
from django.db import models

from .models import Movie


@periodic_task(run_every=crontab(hour=00, minute=00, day_of_week="*"), name="send_daily_report")
def send_daily_report():
    """
    To send report to creators
    """
    creators = Movie.objects.all().values_list('pk', flat=True)
    creators_list = []
    for creator_id in creators:
        movie = Movie.objects.get(id=creator_id)
        creators_list.append(movie.user.email)

    movies = Movie.objects.all()
    average_rating = ""
    for movie in movies:
        stars_average = Movie.objects.get(id=movie.id).rating_set.aggregate(models.Avg('stars')).values()[0]
        average_rating += "Movie : " + movie.title + ", Average Rating : " + str(stars_average) + "\n"

    body = average_rating
    to = creators_list
    sender = settings.EMAIL_HOST_USER
    subject = "Your Daily Report"
    send_mail(subject, body, sender, to, fail_silently=False)
