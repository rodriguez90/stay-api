from rest_framework import serializers

from procedure_resource.models import PersonRequirement, PersonRequirementDocument


class PersonRequirementSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonRequirement
        fields = '__all__'


class PersonRequirementDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonRequirementDocument
        fields = '__all__'
