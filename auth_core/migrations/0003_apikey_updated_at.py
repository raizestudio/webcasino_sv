# Generated by Django 5.1.6 on 2025-03-08 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth_core", "0002_remove_apikey_id_alter_apikey_key"),
    ]

    operations = [
        migrations.AddField(
            model_name="apikey",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
