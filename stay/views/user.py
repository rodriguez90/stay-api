from django.contrib.auth.models import User
from rest_framework import viewsets

from stay.serializers import UserListSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    pagination_class = None
