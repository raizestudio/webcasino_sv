# Generated by Django 5.1.6 on 2025-03-10 09:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('minor_unit', models.IntegerField()),
                ('symbol', models.CharField(max_length=10)),
                ('is_crypto', models.BooleanField(default=False)),
                ('can_deposit', models.BooleanField(default=False)),
                ('can_withdraw', models.BooleanField(default=False)),
                ('is_free', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField()),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial.currency')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField()),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial.currency')),
            ],
        ),
    ]
