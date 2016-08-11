from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer


class Register(APIView):
    """
    Register a new user
    """
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.isvalid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
