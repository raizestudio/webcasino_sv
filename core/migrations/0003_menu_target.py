# Generated by Django 5.1.6 on 2025-03-09 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_menu_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="menu",
            name="target",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
