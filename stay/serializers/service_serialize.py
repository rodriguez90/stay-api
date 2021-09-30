from django.contrib.auth.models import User
from rest_framework import serializers

from stay.models import Service
from .user_serializer import UserSerializer


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'
