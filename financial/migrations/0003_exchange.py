# Generated by Django 5.1.6 on 2025-03-13 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("financial", "0002_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Exchange",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name_plural": "exchanges",
            },
        ),
    ]
