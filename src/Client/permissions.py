from rest_framework.permissions import BasePermission


class ClientPermission(BasePermission):
    message = "Vous n'avez pas les droits pour cela !"

    def has_permission(self, request, view):
        # Ne donnons l’accès qu’aux utilisateurs authentifiés
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        # permet la creation de client au membre du groupe de Gestion et de vente
        if request.method == "POST":
            if "Vente" in request.user.groups:
                return True

        # Permet a tous les utilisateur de voir les clients
        elif request.method == "GET":
            return True

        # Authorise la modification uniquement si l'utilisateur est dnas l'équipe Gestion ou vente
        elif request.method == "PUT" or request.method == "DELETE":
            if "Gestion" in request.user.groups:
                return True
            if "Vente" in request.user.groups:
                if obj.sales_contact == request.user:
                    return True

        else:
            return False
