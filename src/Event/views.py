from rest_framework.viewsets import ModelViewSet
from .serializers import ContractSerializer, EventSerializer
from .permissions import ContractPermission, EventPermission
from .models import Contract, Event
from rest_framework import filters


# Create your views here.
class ContractViewSet(ModelViewSet):

    serializer_class = ContractSerializer
    permission_classes = (ContractPermission,)
    search_fields = ["client__first_name", "client__last_name", "client__email"]
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        return Contract.objects.all()


# Create your views here.
class EventViewSet(ModelViewSet):

    serializer_class = EventSerializer
    permission_classes = (EventPermission,)
    search_fields = ["client__first_name", "client__last_name", "client__email"]
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        return Event.objects.all()
