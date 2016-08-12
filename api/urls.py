from django.conf.urls import patterns, url
from .views import Register

urlpatterns = patterns(
    '',
    url(r'^register/$', Register.as_view(), name='register'),
)
