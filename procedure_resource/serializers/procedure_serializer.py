from rest_framework import serializers

from procedure_resource.models import Procedure


class ProcedureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Procedure
        fields = '__all__'
