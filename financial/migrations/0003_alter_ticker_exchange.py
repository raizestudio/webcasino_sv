# Generated by Django 5.1.6 on 2025-03-14 13:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("financial", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticker",
            name="exchange",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="financial.exchange"
            ),
        ),
    ]
