from rest_framework import viewsets

from stay.models import Service
from stay.serializers import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    """
      This viewset automatically provides list and detail actions
      """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = None
