from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "mobile",
            "compagny_name",
            "date_created",
            "date_updated",
            "converted_client",
            "sales_contact",
        ]
