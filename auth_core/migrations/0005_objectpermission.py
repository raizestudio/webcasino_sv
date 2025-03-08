# Generated by Django 5.1.6 on 2025-03-08 20:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("auth_core", "0004_alter_apikey_client"),
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="ObjectPermission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("object_id", models.CharField(max_length=255)),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="contenttypes.contenttype"
                    ),
                ),
                (
                    "permission",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="auth.permission"),
                ),
            ],
        ),
    ]
