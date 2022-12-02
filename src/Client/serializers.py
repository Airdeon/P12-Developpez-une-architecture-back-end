from rest_framework import serializers
from .models import Client
from datetime import datetime
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
        ]


class ClientSerializer(serializers.ModelSerializer):
    # sales_contact = serializers.StringRelatedField()

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

    def update(self, instance, validated_data):
        instance.date_updated = datetime.now()
        instance.save()
        return super().update(instance, validated_data)
