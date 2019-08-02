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
from rest_framework.authtoken.models import Token

from procedure_resource.models import *
from procedure_resource.serializers import *
# Create your views here.

######
## User gruoup
######
# from django.contrib.auth.models import Group
# my_group = Group.objects.get(name='my_group_name')
# my_group.user_set.add(your_user)


class DepartamentViewSet(viewsets.ModelViewSet):
    """
      This viewset automatically provides list and detail actions
      """
    queryset = Departament.objects.all()
    serializer_class = DepartamentSerializer


class DocumentTypeViewSet(viewsets.ModelViewSet):
    """
      This viewset automatically provides list and detail actions
      """
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer


class ProcedureViewSet(viewsets.ModelViewSet):
    """
      This viewset automatically provides list and detail actions
      """
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer


class ProcedureStepViewSet(viewsets.ModelViewSet):
    """
      This viewset automatically provides list and detail actions
      """
    queryset = ProcedureStep.objects.all()
    serializer_class = ProcedureStepSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
      This viewset automatically provides list and detail actions
      """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


    # def create(self, request, *args, **kwargs):
    #     user_data = request.data.get("user", None)
    #     person_serializer = self.get_serializer(data=request.data)
    #     user_serializer = UserSerializer(data=user_data)
    #     if person_serializer.is_valid(True) and user_serializer.is_valid(True):
    #         user_intance = user_serializer.create()
    #         person = person_serializer.create()
    #
    #         user = None
    #
    #         result = User.objects.filter(username=user_intance.username)
    #         if not result.exists():
    #             user = User.objects.create_user(user_intance.username, user_intance.email, user_intance.password)
    #         else:
    #             user.username = user_intance.username
    #             user.email = user_intance.email
    #             user.password = user_intance.password
    #
    #         # Update fields and then save again
    #         user.first_name = request.data.get("first_name", None)
    #         user.last_name = request.data.get("last_name", None)
    #         user.save()
    #
    #         person = Person.objects.get(id=request.data.get("id", None))
    #
    #         person.user = user
    #         person.save()
    #
    #         # self.perform_create(person_serializer)
    #         headers = self.get_success_headers(person_serializer.data)
    #         #
    #         # person = Person.objects.get(id=request.data.get("id", None))
    #         # person.user = user
    #         # person.save()
    #
    #         return Response(person_serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #
    #         # reponse = super().update(request, args, kwargs)
    #
    #         # return reponse
    #
    #     return Response(person_serializer.data, status=status.HTTP_201_CREATED)

    # def update(self, request, *args, **kwargs):
    #     user_data = request.data.get("user", None)
    #     user_serializer = UserSerializer(data=user_data)
    #     person_serializer = self.get_serializer(data=request.data)
    #     if person_serializer.is_valid(True) and user_serializer.is_valid(True):
    #         user_intance = user_serializer.save()
    #
    #         user = None
    #
    #         result = User.objects.filter(username=user_intance.username)
    #         if not result.exists():
    #             user = User.objects.create_user(user_intance.username, user_intance.email, user_intance.password)
    #         else:
    #             user.username = user_intance.username
    #             user.email = user_intance.email
    #             user.password = user_intance.password
    #
    #         # Update fields and then save again
    #         user.first_name = request.data.get("first_name", None)
    #         user.last_name = request.data.get("last_name", None)
    #         user.save()
    #
    #         person = Person.objects.get(id=request.data.get("id", None))
    #
    #         person.user = user
    #         person.save()
    #
    #         # self.perform_create(person_serializer)
    #         headers = self.get_success_headers(person_serializer.data)
    #         #
    #         # person = Person.objects.get(id=request.data.get("id", None))
    #         # person.user = user
    #         # person.save()
    #
    #         return Response(person_serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #
    #         # reponse = super().update(request, args, kwargs)
    #
    #         # return reponse
    #
    #     return Response(person_serializer.data, status=status.HTTP_201_CREATED)


class PersonProcedureViewSet(viewsets.ModelViewSet):
    """
      This viewset automatically provides list and detail actions
      """
    queryset = PersonProcedure.objects.all()
    serializer_class = PersonProcedureSerializer


class PersonProcedureStepViewSet(viewsets.ModelViewSet):
    """
      This viewset automatically provides list and detail actions
      """
    queryset = PersonProcedureStep.objects.all()
    serializer_class = PersonProcedureStepSerializer


def clean_email(self, username):
    if User.objects.filter(username=username).exists():
        return False

    return True


def clean_username(self, email):
    if User.objects.filter(email=email).exists():
        return False

    return True

