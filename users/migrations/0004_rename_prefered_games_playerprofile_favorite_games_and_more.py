# Generated by Django 5.1.6 on 2025-03-10 21:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_playerprofile_created_at_playerprofile_experience_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="playerprofile",
            old_name="prefered_games",
            new_name="favorite_games",
        ),
        migrations.AddField(
            model_name="playerprofile",
            name="blocked_users",
            field=models.ManyToManyField(blank=True, related_name="blocked_users", to="users.playerprofile"),
        ),
        migrations.AddField(
            model_name="playerprofile",
            name="friends",
            field=models.ManyToManyField(blank=True, related_name="friends", to="users.playerprofile"),
        ),
        migrations.AddField(
            model_name="playerprofile",
            name="referred_user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="referrals",
                to="users.playerprofile",
            ),
        ),
    ]
