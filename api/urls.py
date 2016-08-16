from django.conf.urls import patterns, url
from .views import Register, MovieList

urlpatterns = patterns(
    '',
    url(r'^register/$', Register.as_view(), name='register'),
    url(r'^movies/$', MovieList.as_view(), name='movies'),
)
