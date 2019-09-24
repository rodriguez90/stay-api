from rest_framework import serializers
from django.contrib.auth.models import User

from procedure_resource.models import Procedure, Requirement, DocumentType, RequirementPermission
from .requirement_serializer import RequirementSerializer, RequirementCreateSerializer


class ProcedureSerializer(serializers.ModelSerializer):
    requirements = RequirementSerializer(many=True, read_only=False)

    class Meta:
        model = Procedure
        fields = ['id', 'name', 'description', 'is_active', 'created_at', 'updated_at', 'requirements']
        depth = 1

        related_field = ['requirements']


class ProcedureCreateSerializer(serializers.ModelSerializer):
    requirements = RequirementCreateSerializer(many=True, read_only=False)

    def create(self, validated_data):
        requirements_data = validated_data.pop('requirements')

        procedure = Procedure.objects.create(**validated_data)

        for requirement_data in requirements_data:
            documents = requirement_data.pop('documents')
            permissions = requirement_data.pop('permissions')
            requirement = Requirement.objects.create(procedure=procedure, **requirement_data)

            for docType in documents:
                requirement.documents.add(DocumentType.objects.get(pk=docType.id))

            for user in permissions:
                requirement_permission = RequirementPermission(user=user,
                                                               requirement=requirement)
                # requirement.permissions.add(requirement_permission)
                requirement_permission.save()

            requirement.save()

        return procedure

    class Meta:
        model = Procedure
        fields = ['id', 'name', 'description', 'is_active', 'created_at', 'updated_at', 'requirements']
        related_field = ['requirements']
