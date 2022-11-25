from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = "populate database with needed data"

    def handle(self, *args, **options):

        # Team Gestion
        if not Group.objects.filter(name="Gestion").exists():
            gestion = Group.objects.create(name="Gestion")

            # Right
            # User
            gestion.permissions.add(Permission.objects.get(codename="add_user"))
            gestion.permissions.add(Permission.objects.get(codename="change_user"))
            gestion.permissions.add(Permission.objects.get(codename="delete_user"))
            gestion.permissions.add(Permission.objects.get(codename="view_user"))

            # Client
            gestion.permissions.add(Permission.objects.get(codename="change_client"))
            gestion.permissions.add(Permission.objects.get(codename="view_client"))

            # Contract
            gestion.permissions.add(Permission.objects.get(codename="change_contract"))
            gestion.permissions.add(Permission.objects.get(codename="view_contract"))

            # Contract
            gestion.permissions.add(Permission.objects.get(codename="change_event"))
            gestion.permissions.add(Permission.objects.get(codename="view_event"))

        # Team Vente
        if not Group.objects.filter(name="Vente").exists():
            vente = Group.objects.create(name="Vente")

            # Right
            # Client
            vente.permissions.add(Permission.objects.get(codename="add_client"))
            vente.permissions.add(Permission.objects.get(codename="change_client"))
            vente.permissions.add(Permission.objects.get(codename="view_client"))

            # Contract
            vente.permissions.add(Permission.objects.get(codename="add_contract"))
            vente.permissions.add(Permission.objects.get(codename="change_contract"))
            vente.permissions.add(Permission.objects.get(codename="view_contract"))

            # Event
            vente.permissions.add(Permission.objects.get(codename="add_event"))
            vente.permissions.add(Permission.objects.get(codename="view_event"))

        # Team Support
        if not Group.objects.filter(name="Support").exists():
            support = Group.objects.create(name="Support")

            # Right
            # Event
            support.permissions.add(Permission.objects.get(codename="change_event"))
            support.permissions.add(Permission.objects.get(codename="view_event"))

            # Client
            support.permissions.add(Permission.objects.get(codename="view_client"))
