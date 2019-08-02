from rest_framework import serializers

from procedure_resource.models import DocumentType


class DocumentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DocumentType
        fields = '__all__'
