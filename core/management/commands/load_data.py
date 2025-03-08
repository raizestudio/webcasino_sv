import time
from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Custom command to load fixtures with detailed output'

    def add_arguments(self, parser):
        # Allow the user to pass one or more fixture files as arguments
        # parser.add_argument('fixture', nargs='+', help='List of fixture files to load')
        parser.add_argument('fixture', type=str, help='List of fixture files to load')

    def handle(self, *args, **options):
        start_time = time.time()  # Start measuring time
        fixture = options['fixture']

        result = self.load_fixture(fixture)

        end_time = time.time()
        elapsed_time = round(end_time - start_time, 3)

        app_label = fixture.split('/')[0]
        model_name = fixture.split('/')[-1].split('.')[0]
        
        self.stdout.write(f"Loaded model {model_name} for app {app_label} in {elapsed_time} seconds")

    def load_fixture(self, fixture):
        # Use Django's call_command function to load the fixture and capture the result
        from io import StringIO

        out = StringIO()
        call_command('loaddata', fixture, stdout=out)
        
        # Parse the output to count the number of objects loaded
        output = out.getvalue()
        count = sum(1 for line in output.splitlines() if line.startswith("Installed"))

        return {"fixture": fixture, "count": count}
