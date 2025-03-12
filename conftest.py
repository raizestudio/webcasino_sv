import pytest
from colorama import Back, Fore, Style
from django.contrib.auth import get_user_model
from django.core.management import call_command


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call":
        if result.passed:
            print(Fore.GREEN + "PASSED: " + item.name + Style.RESET_ALL)
        elif result.failed:
            print(Fore.RED + "FAILED: " + item.name + Style.RESET_ALL)
        elif result.skipped:
            print(Fore.YELLOW + "SKIPPED: " + item.name + Style.RESET_ALL)


@pytest.fixture(autouse=True)
def load_fixtures(db):
    print(Fore.CYAN + "Loading fixtures..." + Style.RESET_ALL)
    call_command("loaddata", "dev/currency.json")


@pytest.fixture()
def create_super_user_auth(db):
    get_user_model().objects.create_superuser(email="test@test.io", username="test", password="test")

    print(Fore.CYAN + "Superuser created..." + Style.RESET_ALL)
