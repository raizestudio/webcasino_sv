import sys

import pytest
from django.conf import settings
from django.urls import reverse

from users.models import User


class TestUsersView:
    """Tests for the users endpoint"""

    @pytest.mark.django_db
    def test_users_list_no_auth(self, client):
        """Test users list endpoint without authentication"""
        url = reverse("users-list")
        response = client.get(url)

        assert response.status_code == 403
        assert response.json() == {"detail": "Authentication credentials were not provided."}

    @pytest.mark.django_db
    def test_users_list_user_auth(self, client, create_super_user):
        """Test users list endpoint with user authentication"""
        url = reverse("users-list")
        # _user = User.objects.get(email="test@test.io")

        response = client.get(url)

        # assert response.status_code == 403
        # assert response.json() == {"detail": "You do not have permission to perform this action."}
