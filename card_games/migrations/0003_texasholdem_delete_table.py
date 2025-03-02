# Generated by Django 5.1.6 on 2025-02-28 23:36

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card_games', '0002_deck_table_decks'),
    ]

    operations = [
        migrations.CreateModel(
            name='TexasHoldEm',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deck_cards', models.IntegerField()),
                ('flop_cards', models.IntegerField()),
                ('turn_cards', models.IntegerField()),
                ('river_cards', models.IntegerField()),
                ('small_blind', models.IntegerField()),
                ('big_blind', models.IntegerField()),
                ('ante', models.IntegerField()),
                ('max_players', models.IntegerField()),
                ('min_players', models.IntegerField()),
                ('max_rounds', models.IntegerField()),
                ('max_raise', models.IntegerField()),
                ('max_bet', models.IntegerField()),
                ('max_call', models.IntegerField()),
                ('max_check', models.IntegerField()),
                ('max_fold', models.IntegerField()),
                ('max_all_in', models.IntegerField()),
                ('max_showdown', models.IntegerField()),
                ('timeout', models.IntegerField()),
                ('decks', models.ManyToManyField(related_name='tables', to='card_games.deck')),
            ],
            options={
                'verbose_name_plural': 'tables',
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Table',
        ),
    ]
