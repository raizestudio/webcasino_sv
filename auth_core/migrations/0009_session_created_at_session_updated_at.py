# Generated by Django 5.1.6 on 2025-03-09 22:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth_core", "0008_session_token"),
    ]

    operations = [
        migrations.AddField(
            model_name="session",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="session",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
