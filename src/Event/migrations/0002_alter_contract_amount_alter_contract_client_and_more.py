# Generated by Django 4.1.3 on 2022-11-18 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Client", "0001_initial"),
        ("Event", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contract",
            name="amount",
            field=models.FloatField(verbose_name="Montant"),
        ),
        migrations.AlterField(
            model_name="contract",
            name="client",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="Client.client",
                verbose_name="Client",
            ),
        ),
        migrations.AlterField(
            model_name="contract",
            name="date_updated",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Date de mise a jour"
            ),
        ),
        migrations.AlterField(
            model_name="contract",
            name="payment_due",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Date de payement"
            ),
        ),
        migrations.AlterField(
            model_name="contract",
            name="sales_contact",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Vendeur",
            ),
        ),
        migrations.AlterField(
            model_name="contract",
            name="status",
            field=models.BooleanField(default=False, verbose_name="Contrat signé ?"),
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Date de création"
                    ),
                ),
                (
                    "date_updated",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Date de mise a jour"
                    ),
                ),
                ("attendees", models.PositiveSmallIntegerField(verbose_name="Montant")),
                (
                    "event_date",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Date de l'evènement"
                    ),
                ),
                ("notes", models.TextField(verbose_name="Notes")),
                (
                    "client",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="Client.client",
                        verbose_name="Client",
                    ),
                ),
                (
                    "contract",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Event.contract",
                        verbose_name="Support",
                    ),
                ),
                (
                    "support_contact",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Support",
                    ),
                ),
            ],
            options={
                "ordering": ["id"],
            },
        ),
    ]
