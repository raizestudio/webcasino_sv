# Generated by Django 5.1.6 on 2025-03-10 14:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Menu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("path", models.CharField(max_length=100)),
                ("target", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="core.menu",
                    ),
                ),
            ],
            options={
                "verbose_name": "Menu",
                "verbose_name_plural": "Menus",
            },
        ),
    ]
