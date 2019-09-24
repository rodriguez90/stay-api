from django.contrib.auth.models import User

from rest_framework import serializers

from procedure_resource.models import Requirement, RequirementPermission
from .user_serializer import UserSerializer, UserListSerializer
from .document_type_serializer import DocumentTypeSerializer
from .departement_serializer import DepartamentSerializer
from .requirement_permission_serializer import RequirementPermissionSerializer


class RequirementSerializer(serializers.ModelSerializer):
    # permissions = RequirementPermissionSerializer(many=True, read_only=True)
    # documents = DocumentTypeSerializer(many=True, read_only=False)
    # departament = DepartamentSerializer(read_only=False)

    class Meta:
        model = Requirement
        fields = '__all__'
        depth = 1

        # related_field = ['documents', 'departament', 'permissions']


class RequirementCreateSerializer(serializers.ModelSerializer):

    permissions = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Requirement
        fields = ['id', 'departament', 'documents', 'permissions', 'name', 'description', 'position', 'is_active']

        related_field = ['permissions', 'documents', 'departament']
