from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.contrib.contenttypes.models import ContentType
from django.db import models

from auth_core.models import ObjectPermission


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)

        if password:
            user.set_password(password)  # This hashes the password properly

        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, email, password, **extra_fields)

    def get_by_natural_key(self, email):
        return self.get(email=email)

    def get_active_users(self):
        return self.filter(is_active=True)


class User(AbstractBaseUser, PermissionsMixin):
    """The custom user model"""

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """
        Check if the user has a specific permission on the target object.
        """

        if obj is None:
            # Global permission check
            return super().has_perm(perm)

        # Get the content type for the target object
        content_type = ContentType.objects.get_for_model(obj)

        # Query ObjectPermission to check if the user has permission on this object
        permission = ObjectPermission.objects.filter(
            permission__codename=perm,
            owner_object_id=str(self.pk),
            owner_content_type=ContentType.objects.get_for_model(self),
            target_object_id=str(obj.pk),
            target_content_type=content_type,
        ).exists()

        return permission

    def get_all_permissions(self):
        """
        Return a set of permission strings that the user has.
        """
        permissions = ObjectPermission.objects.filter(
            owner_object_id=str(self.pk),
            owner_content_type=ContentType.objects.get_for_model(self),
        ).values_list("permission__codename", "target_object_id", "target_content_type")

        return permissions


class UserSecurity(models.Model):
    """The user security model"""

    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    is_two_factor_enabled = models.BooleanField(default=False)
    antiphishing_code = models.CharField(max_length=6, blank=True, null=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="security")


class UserPreferences(models.Model):
    """The user preferences model"""

    is_email_notification_enabled = models.BooleanField(default=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="preferences")


class PlayerProfile(models.Model):
    """The player profile model"""

    updated_at = models.DateTimeField(auto_now=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="player_profile")
    prefered_games = models.ManyToManyField("games.Game", related_name="players", blank=True)
