from celery.task.schedules import crontab
from celery.decorators import periodic_task
from django.conf import settings
from django.core.mail import send_mail

from .models import Movie


@periodic_task(run_every=crontab(hour=0, minute=0, day_of_week="*"))
def send_daily_report(pk):
    """
    send report to admins
    """
    remind = Movie.objects.get(pk=pk)
    body = remind.message
    to = [remind.email, ]
    sender = settings.EMAIL_HOST_USER
    subject = "Your Reminder"
    send_mail(subject, body, sender, to, fail_silently=False)