# Generated by Django 5.1.6 on 2025-03-08 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth_core", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="apikey",
            name="id",
        ),
        migrations.AlterField(
            model_name="apikey",
            name="key",
            field=models.CharField(max_length=128, primary_key=True, serialize=False),
        ),
    ]
