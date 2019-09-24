from django.contrib.auth.models import User
from rest_framework import serializers

from procedure_resource.models import RequirementPermission

from .user_serializer import UserSerializer, UserListSerializer


class RequirementPermissionSerializer(serializers.ModelSerializer):
    # user = UserListSerializer(many=False, read_only=True)
    # requirement = serializers.SlugRelatedField(slug_field='requirement', queryset=Re)

    class Meta:
        model = RequirementPermission
        # fields = ['id', 'user', 'is_active', 'created_at', 'updated_at']
        # fields = ['id', 'user']
        fields = '__all__'
        # exclude = ['requirement']
        depth = 1

        # related_field = ['user', 'requirement']
        # related_field = ['user']
