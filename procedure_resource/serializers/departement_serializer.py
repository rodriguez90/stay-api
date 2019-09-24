from rest_framework import serializers

from procedure_resource.models import Departament


class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departament
        fields = '__all__'
