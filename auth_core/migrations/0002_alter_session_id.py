# Generated by Django 5.1.6 on 2025-03-10 10:01

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
