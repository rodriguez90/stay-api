from rest_framework import serializers
from django.contrib.auth.models import User
from procedure_resource.models import UserProcedurePermission


class UserProcedurePermissionSerializer(serializers.ModelSerializer):
    user = serializers.ManyRelatedField(many=True)
    procedure = serializers.ManyRelatedField(many=True)

    class Meta:
        model = UserProcedurePermission
        fields = ['id', 'user', 'is_active', 'procedure', 'created_at', 'updated_at']
