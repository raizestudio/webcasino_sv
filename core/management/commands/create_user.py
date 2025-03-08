from django.contrib.auth import get_user_model
from django.core.management import CommandError
from django.core.management.base import BaseCommand, CommandError
from django.db.transaction import atomic

from financial.models import Currency, Wallet
from users.models import PlayerProfile, UserSecurity, UserPreferences


class Command(BaseCommand):
    help = "Create a superuser"

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument("--email", type=str, help="Email for the user")
        parser.add_argument("--username", type=str, help="Username for the user")
        parser.add_argument("--password", type=str, help="Password for the user")
        parser.add_argument("--is-staff", type=bool, help="Is staff for the user")

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Creating user..."))

        if not options.get("email"):
            raise CommandError("The --email option is required.")

        if not options.get("username"):
            raise CommandError("The --username option is required.")

        if not options.get("password"):
            raise CommandError("The --password option is required.")

        with atomic():
            User = get_user_model()
            _user = User.objects.create_user(
                username=options["username"],
                email=options["email"],
                password=options["password"],
            )
            if options.get("is_staff"):
                _user.is_staff = True
                
            _user.save()
            _free_currency = Currency.objects.get(code="tkn")
            _wallet = Wallet.objects.create(user=_user, currency=_free_currency, balance=1000)
            _user_security = UserSecurity.objects.create(user=_user)
            _user_preferences = UserPreferences.objects.create(user=_user)

        self.stdout.write(self.style.SUCCESS(f"User created successfully: {_user.email}"))
