from django.http import Http404

from rest_framework.permissions import BasePermission

from .models import Movie, Rating


class IsNotOwner(BasePermission):
    """
    Allow users who have not added the movie to rate the movie once.
    """
    def has_permission(self, request, view):
        try:
            movie = Movie.objects.get(pk=request.data['movie'])
        except Movie.DoesNotExist:
            raise Http404
        if request.user != movie.user:
            try:
                Rating.objects.get(user=request.user)
                return False
            except Rating.DoesNotExist:
                return True
        return False
