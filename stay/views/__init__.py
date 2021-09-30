from .auth import RegisterView
from .user import UserViewSet
from .person import PersonViewSet
from .rent import RentViewSet
from .service import ServiceViewSet

# django
from django.shortcuts import render
from django.contrib.auth.models import User

# rest_framework
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import status
from rest_framework import viewsets
from rest_framework import authentication
from rest_framework_jwt.authentication import  JSONWebTokenAuthentication
from rest_framework.generics import *
from rest_framework.mixins import *
from rest_framework.authtoken.models import Token

from stay.models import *
from stay.serializers import *
# Create your views here.

from stay.views import *


def clean_email(self, username):
    if User.objects.filter(username=username).exists():
        return False

    return True


def clean_username(self, email):
    if User.objects.filter(email=email).exists():
        return False

    return True

