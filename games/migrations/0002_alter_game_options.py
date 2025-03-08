# Generated by Django 5.1.6 on 2025-03-08 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("games", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="game",
            options={
                "ordering": ["-created_at"],
                "permissions": [("can_play", "Can play the game"), ("can_review", "Can review the game")],
            },
        ),
    ]
