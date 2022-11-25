# Generated by Django 4.1.3 on 2022-11-24 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Client", "0004_alter_client_compagny_name_alter_client_date_updated"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="sales_contact",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"group__name": "Vente"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="client_sales_contact",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Vendeur",
            ),
        ),
    ]
