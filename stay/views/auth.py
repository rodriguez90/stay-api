from rest_framework.generics import CreateAPIView
from rest_framework import permissions

from stay.serializers import PersonSerializer


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
