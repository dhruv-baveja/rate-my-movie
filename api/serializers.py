from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, data):
        user = User.objects.create(
            username=data['username'],
            email=data['email']
        )
        user.set_password(data['password'])
        user.save()
        return user
