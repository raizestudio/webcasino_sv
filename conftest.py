import pytest
from colorama import Back, Fore, Style
from django.apps import apps
from django.contrib.auth import get_user_model
from django.core.management import call_command
from knox.models import get_token_model


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
    _user = get_user_model().objects.create_superuser(email="test@test.io", username="test", password="test")

    token_model = get_token_model()
    _token_instance, raw_token = token_model.objects.create(get_user_model().objects.get(email="test@test.io"))
    print(Fore.CYAN + f"Superuser created as {_user} with token {_token_instance}..." + Style.RESET_ALL)
    return raw_token


@pytest.fixture()
def create_api_key():
    api_key_client_model = apps.get_model("auth_core", "APIKeyClient")
    api_key_client = api_key_client_model.objects.create(name="Test API Key Client")

    api_key_model = apps.get_model("auth_core", "APIKey")
    api_key = api_key_model.objects.create(client=api_key_client)

    print(Fore.CYAN + "API Key Client created..." + Style.RESET_ALL)
    return api_key
