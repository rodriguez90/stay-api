from rest_framework import viewsets
from stay.models import Person
from stay.serializers import PersonSerializer


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
