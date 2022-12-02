from rest_framework.viewsets import ModelViewSet
from .serializers import ClientSerializer
from .permissions import ClientPermission
from .models import Client

# Create your views here.
class ClientViewSet(ModelViewSet):

    serializer_class = ClientSerializer
    permission_classes = (ClientPermission,)

    def get_queryset(self):
        return Client.objects.all()
