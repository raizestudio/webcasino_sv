from django.core.management import BaseCommand, CommandError, call_command

from core.tasks import fetch_api_data

DEV_USERS = [
    {
        "email": "t@t.io",
        "username": "test",
        "password": "test",
        "is_staff": False,
    },
    {
        "email": "m@m.io",
        "username": "mod",
        "password": "mod",
        "is_staff": True,
    },
]


class Command(BaseCommand):

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument("--no-root", action="store_true", help="Do not create the default superuser")
        parser.add_argument("--no-users", action="store_true", help="Do not create dev users")
        parser.add_argument("--no-fixtures", action="store_true", help="Do not load fixtures")
        parser.add_argument("--no-migrations", action="store_true", help="Do not run migrations")

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Starting installation..."))
        call_command("makemigrations")
        call_command("flush", "--noinput")
        # call_command("migrate", verbosity=0)
        call_command("migrate")

        if not options.get("no_fixtures"):
            call_command("load_fixtures")

        if not options.get("no_root"):
            call_command("create_super_user", "--email", "r@r.io", "--username", "root", "--password", "root")

        if not options.get("no_users"):
            for user in DEV_USERS:
                if user.get("is_staff"):
                    call_command(
                        "create_user",
                        f"--email={user['email']}",
                        f"--username={user['username']}",
                        f"--password={user['password']}",
                        f"--is-staff={user['is_staff']}",
                    )
                else:
                    call_command(
                        "create_user",
                        f"--email={user['email']}",
                        f"--username={user['username']}",
                        f"--password={user['password']}",
                    )

        self.stdout.write(self.style.NOTICE("Fetching global data..."))
        fetch_api_data.delay()

        self.stdout.write(self.style.SUCCESS("All done!"))
