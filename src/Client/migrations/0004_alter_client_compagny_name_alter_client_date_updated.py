# Generated by Django 4.1.3 on 2022-11-24 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Client", "0003_alter_client_email_alter_client_mobile_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="compagny_name",
            field=models.CharField(max_length=250, verbose_name="Entreprise"),
        ),
        migrations.AlterField(
            model_name="client",
            name="date_updated",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Date de mise a jour"
            ),
        ),
    ]