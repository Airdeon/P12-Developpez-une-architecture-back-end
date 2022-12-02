from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group


class ClientPermission(BasePermission):
    message = "Vous n'avez pas les droits pour cela !"

    def has_permission(self, request, view):
        # Ne donnons l’accès qu’aux utilisateurs authentifiés
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        # permet la creation de client au membre du groupe de Gestion et de vente
        if request.method == "POST":
            if Group.objects.get(name="Vente") in request.user.groups.all():
                return True

        # Permet a tous les utilisateur de voir les clients
        elif request.method == "GET":
            return True

        # Authorise la modification uniquement si l'utilisateur est dnas l'équipe Gestion ou vente
        elif request.method == "PUT" or request.method == "DELETE":
            if Group.objects.get(name="Gestion") in request.user.groups.all():
                return True
            if Group.objects.get(name="Vente") in request.user.groups.all():
                if obj.sales_contact == request.user:
                    return True

        else:
            return False
