from rest_framework.viewsets import ModelViewSet
from .serializers import ClientSerializer
from .permissions import ClientPermission
from .models import Client
from rest_framework import filters


# Create your views here.
class ClientViewSet(ModelViewSet):

    serializer_class = ClientSerializer
    permission_classes = (ClientPermission,)
    search_fields = ["first_name", "last_name", "email"]
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        return Client.objects.all()
