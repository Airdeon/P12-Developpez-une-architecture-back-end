from rest_framework import serializers
from .models import Contract, Event
from datetime import datetime


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = [
            "id",
            "sales_contact",
            "client",
            "date_created",
            "date_updated",
            "status",
            "amount",
            "payment_due",
        ]

    def update(self, instance, validated_data):
        instance.date_updated = datetime.now()
        instance.save()
        return super().update(instance, validated_data)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "client",
            "date_created",
            "date_updated",
            "support_contact",
            "contract",
            "attendees",
            "event_date",
            "notes",
        ]

    def update(self, instance, validated_data):
        instance.date_updated = datetime.now()
        instance.save()
        return super().update(instance, validated_data)
