from django.db import models
from django.contrib.auth.models import User
from Client.models import Client


# Create your models here.
class Contract(models.Model):
    sales_contact = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        limit_choices_to={"groups__name": "Vente"},
        null=True,
        verbose_name="Vendeur",
        related_name="contract_sales_contact",
    )
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, verbose_name="Client")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    date_updated = models.DateTimeField(null=True, blank=True, verbose_name="Date de mise a jour")
    status = models.BooleanField(default=False, verbose_name="Contrat signé ?")
    amount = models.FloatField(verbose_name="Montant")
    payment_due = models.DateTimeField(null=True, blank=True, verbose_name="Date de payement")

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return str(self.date_created) + " : " + str(self.client)


# Create your models here.
class Event(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.SET_NULL, null=True, verbose_name="Client", related_name="event_client"
    )
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    date_updated = models.DateTimeField(null=True, blank=True, verbose_name="Date de mise a jour")
    support_contact = models.ForeignKey(
        User, on_delete=models.SET_NULL, limit_choices_to={"groups__name": "Support"}, null=True, verbose_name="Support"
    )
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True, verbose_name="Contrat")
    attendees = models.PositiveSmallIntegerField(verbose_name="Nombre de personne attendu")
    event_date = models.DateTimeField(null=True, blank=True, verbose_name="Date de l'evènement")
    notes = models.TextField(blank=True, null=True, verbose_name="Notes")

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return str(self.date_created) + " : " + str(self.client)
