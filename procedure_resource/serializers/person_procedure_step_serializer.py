from rest_framework import serializers

from procedure_resource.models import PersonProcedureStep, PersonProcedureStepDocument


class PersonProcedureStepSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonProcedureStep
        fields = '__all__'


class PersonProcedureStepDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonProcedureStepDocument
        fields = '__all__'
