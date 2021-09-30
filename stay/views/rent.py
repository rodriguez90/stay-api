from rest_framework import viewsets

from stay.models import Rent
from stay.serializers import RentSerializer, RentCreateSerializer


class RentViewSet(viewsets.ModelViewSet):
    """
      This viewset automatically provides list and detail actions
      """
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    pagination_class = None

    action_serializers = {
        'retrieve': RentSerializer,
        'list': RentSerializer,
        'create': RentCreateSerializer,
        'update': RentCreateSerializer
    }

    def get_serializer_class(self):

        if hasattr(self, 'action_serializers'):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]

        return super(RentViewSet, self).get_serializer_class()
