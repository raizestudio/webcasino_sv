import sys

import pytest
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

from users.serializers import UserSerializer


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
    def test_users_list_user_auth(self, client, create_super_user_auth):
        """Test users list endpoint with user authentication"""
        url = reverse("users-list")

        _token = create_super_user_auth
        print(f"Token: {_token}")
        response = client.get(url, headers={"Authorization": f"Token {_token}"})

        users = UserSerializer(get_user_model().objects.all(), many=True).data

        assert response.status_code == 200
        assert response.json() == users

    @pytest.mark.django_db
    def test_users_list_api_key_auth(self, client, create_api_key):
        """Test users list endpoint with user authentication"""
        url = reverse("users-list")

        _api_key = create_api_key
        response = client.get(url, headers={"x-api-key": _api_key.key})

        users = UserSerializer(get_user_model().objects.all(), many=True).data

        assert response.status_code == 200
        assert response.json() == users
