import sys
from pathlib import Path

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError

AVAILABLE_FIXTURES = [
    # geo
    "geo.continent",
    # financial
    "financial.currency",
    # games
    "games.gamecategory",
    "games.game",
]


class Command(BaseCommand):

    def add_arguments(self, parser):
        return super().add_arguments(parser)

    def handle(self, *args, **options):
        sys.stderr.write("Loading fixtures.\n")
        for fixture in AVAILABLE_FIXTURES:
            try:
                fname = fixture.split(".")[-1]
                call_command("loaddata", fname)
            except IntegrityError as e:
                sys.stderr.write(f"Error loading {fixture}: {e}\n")
