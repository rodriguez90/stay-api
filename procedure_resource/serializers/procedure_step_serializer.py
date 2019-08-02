from rest_framework import serializers

from procedure_resource.models import ProcedureStep


class ProcedureStepSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProcedureStep
        fields = '__all__'
