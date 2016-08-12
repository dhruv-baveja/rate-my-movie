from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.authtoken import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^api/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-token-auth/', views.obtain_auth_token),
)
