from django.contrib import admin
from .models import Event, Contract

# Register your models here.
# admin.site.register(Event)
# admin.site.register(Contract)


@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    def get_queryset(self, request):
        super().get_queryset(request)
        if request.user.groups.filter(name="Gestion").exists() or request.user.username == "admin":
            return Event.objects.all()
        elif request.user.groups.filter(name="Vente").exists():
            return Event.objects.filter(client__sales_contact=request.user)
        elif request.user.groups.filter(name="Support").exists():
            return Event.objects.filter(support_contact=request.user)


@admin.register(Contract)
class AdminContract(admin.ModelAdmin):
    def get_queryset(self, request):
        super().get_queryset(request)
        if request.user.groups.filter(name="Gestion").exists() or request.user.username == "admin":
            return Contract.objects.all()
        elif request.user.groups.filter(name="Vente").exists():
            return Contract.objects.filter(sales_contact=request.user)
        elif request.user.groups.filter(name="Support").exists():
            return Contract.objects.filter(event_set__support_contact=request.user)
