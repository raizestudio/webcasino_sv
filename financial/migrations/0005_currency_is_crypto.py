# Generated by Django 5.1.6 on 2025-03-15 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("financial", "0004_alter_ticker_csupply_alter_ticker_msupply_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="currency",
            name="is_crypto",
            field=models.BooleanField(default=False),
        ),
    ]
