from django.contrib import admin
from .models import Client
from django.contrib.auth.models import Group

# Register your models here.
@admin.register(Client)
class AdminClient(admin.ModelAdmin):
    def get_queryset(self, request):
        super().get_queryset(request)
        if Group.objects.get(name="Gestion") in request.user.groups.all() or request.user.username == "admin":
            return Client.objects.all()
        elif Group.objects.get(name="Vente") in request.user.groups.all():
            return Client.objects.filter(sales_contact=request.user)
        elif Group.objects.get(name="Support") in request.user.groups.all():
            # return Event.objects.filter(support_contact=request.user).client.all()
            return Client.objects.filter(event_client__support_contact=request.user)


# admin.site.register(AdminClient)
