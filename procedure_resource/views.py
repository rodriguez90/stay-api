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

from procedure_resource.models import *
from procedure_resource.serializers import *
# Create your views here.


class RegisterView(CreateAPIView):
    serializer_class = PersonSerializer
    permissions = permissions.AllowAny
    permission_classes = []
    authentication_classes = []

    # def create(self, request, *args, **kwargs):
    #     user_data = request.data.get("user", None)
    #     person_serializer = self.get_serializer(data=request.data)
    #     user_serializer = UserSerializer(data=user_data)
    #     if person_serializer.is_valid(True) and user_serializer.is_valid(True):
    #         user_intance = user_serializer.create(validated_data=user_data)
    #         person = person_serializer.create(request.data)
    #
    #         user = None
    #
    #         result = User.objects.filter(username=user_intance.username)
    #         if not result.exists():
    #             user_intance = User.objects.create_user(user_intance.username, user_intance.email, user_intance.password)
    #             person = person_serializer.create(request.data)
    #             person.user = user_intance
    #             person.save()
    #
    #             return Response(person_serializer.data, status=status.HTTP_201_CREATED)
    #         else:
    #             return Response(person_serializer.data, status=status.HTTP_400_BAD_REQUEST,)
    #
    #     return Response(person_serializer.data, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    pagination_class = None


class DepartamentViewSet(viewsets.ModelViewSet):
    """
      This viewset automatically provides list and detail actions
      """
    queryset = Departament.objects.all()
    serializer_class = DepartamentSerializer
    pagination_class = None

    # permissions = permissions.AllowAny
    # permission_classes = []
    # authentication_classes = []


class DocumentTypeViewSet(viewsets.ModelViewSet):
    """
      This viewset automatically provides list and detail actions
      """
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer
    pagination_class = None

    # permissions = permissions.AllowAny
    # permission_classes = []
    # authentication_classes = []


class ProcedureViewSet(viewsets.ModelViewSet):
    """
      This viewset automatically provides list and detail actions
      """
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer
    pagination_class = None

    action_serializers = {
        'retrieve': ProcedureSerializer,
        'list': ProcedureSerializer,
        'create': ProcedureCreateSerializer,
        'update': ProcedureCreateSerializer
    }

    def get_serializer_class(self):

        if hasattr(self, 'action_serializers'):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]

        return super(RequirementViewSet, self).get_serializer_class()


class RequirementViewSet(viewsets.ModelViewSet):
    """
      This viewset automatically provides list and detail actions
      """
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer
    pagination_class = None

    action_serializers = {
        'retrieve': RequirementSerializer,
        'list': RequirementSerializer,
        'create': RequirementCreateSerializer,
        'update': RequirementSerializer
    }

    def get_serializer_class(self):

        if hasattr(self, 'action_serializers'):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]

        return super(RequirementViewSet, self).get_serializer_class()


class PersonViewSet(viewsets.ModelViewSet):
    """
      This viewset automatically provides list and detail actions
      """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    pagination_class = None


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
    pagination_class = None


class PersonProcedureStepViewSet(viewsets.ModelViewSet):
    """
      This viewset automatically provides list and detail actions
      """
    queryset = PersonRequirement.objects.all()
    serializer_class = PersonRequirementSerializer
    pagination_class = None


def clean_email(self, username):
    if User.objects.filter(username=username).exists():
        return False

    return True


def clean_username(self, email):
    if User.objects.filter(email=email).exists():
        return False

    return True

