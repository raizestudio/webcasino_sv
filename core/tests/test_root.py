import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_root_view(client):
    url = reverse("root-view")  # Make sure this matches your URL name
    response = client.get(url)

    assert response.status_code == 200
    assert response.json() == {"message": "Should i call you mistah?"}
