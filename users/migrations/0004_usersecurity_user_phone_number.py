# Generated by Django 5.1.6 on 2025-03-08 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_user_created_at_playerprofile_delete_player"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserSecurity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("is_email_verified", models.BooleanField(default=False)),
                ("is_phone_verified", models.BooleanField(default=False)),
                ("is_two_factor_enabled", models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="phone_number",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
