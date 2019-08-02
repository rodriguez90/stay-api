from rest_framework import serializers

from procedure_resource.models import Person, PersonProcedure
from .user_serializer import UserSerializer


class PersonSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True, allow_null=True)

    # def is_valid(self, raise_exception=False):
    #     is_valid = super().is_valid(False)
    #     errors = self.errors
    #     data = self.validated_data
    #     return is_valid

    # def create(self, validated_data):
    #     user_serialized = UserSerializer(validated_data["user"])
    #     user_serialized.create()
    #     super().update()

    class Meta:
        model = Person
        fields = [
            'id',
            'first_name',
            'second_name',
            'last_name',
            'second_last_name',
            'identification',
            'email',
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


