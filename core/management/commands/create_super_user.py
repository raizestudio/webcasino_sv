from django.contrib.auth.management.commands.createsuperuser import (
    Command as BaseCreateSuperUserCommand,
)
from django.core.management import CommandError


class Command(BaseCreateSuperUserCommand):
    help = "Create a superuser"

    def add_arguments(self, parser):
        super().add_arguments(parser)
        # parser.add_argument("--custom-field", type=str, help="Custom field for the superuser")

    def handle(self, *args, **options):
        print("Custom createsuperuser command is running...")  # Debug

        # custom_field = options.get("custom_field")

        # if not custom_field:
        #     raise CommandError("The --custom-field option is required.")

        super().handle(*args, **options)

        from django.contrib.auth import get_user_model

        User = get_user_model()
        # user = User.objects.get(username=options["username"])
        # user.custom_field = custom_field
        # user.save()

        # self.stdout.write(self.style.SUCCESS(f"Superuser created with custom field: {custom_field}"))
        self.stdout.write(self.style.SUCCESS(f"Superuser created with custom field: "))
