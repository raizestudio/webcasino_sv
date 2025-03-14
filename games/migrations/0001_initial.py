# Generated by Django 5.1.6 on 2025-03-14 13:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GameCategory",
            fields=[
                ("code", models.CharField(max_length=10, primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("order", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Game",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("release_date", models.DateField(null=True)),
                ("rating", models.FloatField(default=0)),
                ("preview_image", models.ImageField(blank=True, null=True, upload_to="games")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="games.gamecategory"),
                ),
            ],
            options={
                "ordering": ["-created_at"],
                "permissions": [("can_play", "Can play the game"), ("can_review", "Can review the game")],
            },
        ),
        migrations.CreateModel(
            name="Slot",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("reels", models.IntegerField(default=3)),
                ("rows", models.IntegerField(default=3)),
                ("paylines", models.IntegerField(default=1)),
                ("min_bet", models.FloatField(default=0)),
                ("max_bet", models.FloatField(default=0)),
                ("buy_feature", models.BooleanField(default=False)),
                ("bonus_game", models.BooleanField(default=False)),
                ("free_spins", models.BooleanField(default=False)),
                ("jackpot", models.BooleanField(default=False)),
                (
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="slots", to="games.game"
                    ),
                ),
            ],
        ),
    ]
