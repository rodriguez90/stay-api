from django.contrib.auth.models import User
from rest_framework import serializers

from procedure_resource.models import Person, PersonProcedure
from .user_serializer import UserSerializer


class PersonSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=False)

    # def is_valid(self, raise_exception=False):
    #     is_valid = super().is_valid(False)
    #     errors = self.errors
    #     data = self.validated_data
    #     return is_valid

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        # user = self.user.create(user_data)

        person = Person.objects.create(user=user, **validated_data)
        return person

    class Meta:
        model = Person
        fields = [
            'second_name',
            'second_last_name',
            'identification',
            'phone_number',
            'address',
            'is_active',
            'created_at',
            'updated_at',
            'user'
        ]
        related_field = ["user"]


class PersonProcedureSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonProcedure
        fields = '__all__'


