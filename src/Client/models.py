from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=25, verbose_name="Prenom")
    last_name = models.CharField(max_length=25, verbose_name="Nom")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="Email")
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Téléphone")
    mobile = models.CharField(max_length=20, null=True, blank=True, verbose_name="Mobile")
    compagny_name = models.CharField(max_length=250, verbose_name="Entreprise")
    date_created = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Date de création")
    date_updated = models.DateTimeField(null=True, blank=True, verbose_name="Date de mise a jour")
    converted_client = models.BooleanField(default=False, verbose_name="Client converti")
    sales_contact = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        limit_choices_to={"groups__name": "Vente"},
        null=True,
        blank=True,
        verbose_name="Vendeur",
        related_name="client_sales_contact",
    )

    class Meta:
        ordering = ["last_name"]

    def __str__(self):
        return self.last_name + " " + self.first_name
