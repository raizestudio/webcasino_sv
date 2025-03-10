import pytest
from django.conf import settings
from django.urls import reverse


@pytest.mark.django_db
def test_root_view(client):
    url = reverse("root-view")
    response = client.get(url)

    assert response.status_code == 200
    assert response.json() == {"detail": "Should i call you mistah?", "api_version": settings.API_VERSION}
