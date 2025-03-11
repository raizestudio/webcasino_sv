from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Gather coins data from different sources"

    