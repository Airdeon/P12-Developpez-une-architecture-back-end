from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group


class ContractPermission(BasePermission):
    message = "Vous n'avez pas les droits pour cela !"

    def has_permission(self, request, view):
        # Ne donnons l’accès qu’aux utilisateurs authentifiés
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        # permet la creation de contrat au membre du groupe de Gestion et de vente
        if request.method == "POST":
            if Group.objects.get(name="Vente") in request.user.groups.all():
                return True

        # Permet a tous les utilisateur de voir les contrat
        elif request.method == "GET":
            return True

        # Authorise la modification uniquement si l'utilisateur est dans l'équipe Gestion ou vente
        elif request.method == "PUT":
            if Group.objects.get(name="Gestion") in request.user.groups.all():
                return True
            if Group.objects.get(name="Vente") in request.user.groups.all():
                if obj.sales_contact == request.user:
                    return True

        elif request.method == "DELETE":
            if Group.objects.get(name="Gestion") in request.user.groups.all():
                return True

        else:
            return False


class EventPermission(BasePermission):
    message = "Vous n'avez pas les droits pour cela !"

    def has_permission(self, request, view):
        # Ne donnons l’accès qu’aux utilisateurs authentifiés
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, event_object):
        # permet la creation de client au membre du groupe de Gestion et de vente
        if request.method == "POST":
            if Group.objects.get(name="Vente") in request.user.groups.all():
                return True

        # Permet a tous les utilisateur de voir les clients
        elif request.method == "GET":
            return True

        # Authorise la modification uniquement si l'utilisateur est dans l'équipe Gestion ou qu'il gère l'évènement
        elif request.method == "PUT":
            if Group.objects.get(name="Gestion") in request.user.groups.all():
                return True
            if Group.objects.get(name="Vente") in request.user.groups.all():
                if event_object.client.sales_contact == request.user:
                    return True
            if Group.objects.get(name="Support") in request.user.groups.all():
                if event_object.support_contact == request.user:
                    return True

        elif request.method == "DELETE":
            if Group.objects.get(name="Gestion") in request.user.groups.all():
                return True

        else:
            return False
