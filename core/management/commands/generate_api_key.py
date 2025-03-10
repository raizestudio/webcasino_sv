import uuid

from django.core.management import CommandError
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError

from auth_core.models import APIKey, APIKeyClient


class Command(BaseCommand):
    help = "Generate an API key for a user"

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument("--client", type=str, help="Client email for the API key")
        parser.add_argument("--client-name", type=str, help="Client name for the API key, required if --create is set")
        parser.add_argument("--create", action="store_true", help="Create the client for API key")
        parser.add_argument("--generate", action="store_true", help="Generate new API key")

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Generating API key..."))

        if not options.get("client"):
            raise CommandError("The --client option is required.")

        if options.get("create") and not options.get("client_name"):
            raise CommandError("The --client_name option is required if --create is set.")

        if options.get("create"):
            try:
                _client = APIKeyClient.objects.create(email=options["client"], name=options["client_name"])

            except IntegrityError:
                raise CommandError(f"Client with email {options['client']} already exists, remove --create option.")
        else:
            _client = APIKeyClient.objects.get(email=options["client"])

        try:
            _api_key = APIKey.objects.create(client=_client)

        except IntegrityError:
            if not options.get("generate"):
                _api_key = APIKey.objects.get(client=_client)
                raise CommandError(f"Client {options['client']} already has an issued key: {_api_key.key}.")
            else:
                _api_key = APIKey.objects.get(client=_client)
                api_key_bk = _api_key.key
                _api_key.key = uuid.uuid4()
                _api_key.save()
                self.stdout.write(self.style.ERROR(f"Client {options['client']} key was {api_key_bk} -> {_api_key.key}."))

        self.stdout.write(self.style.SUCCESS(f"API key generated successfully: {_api_key.key}"))
