import uuid

from django.contrib.contenttypes.models import ContentType
from django.db import models
from knox.models import AuthToken


class ObjectPermissionManager(models.Manager):
    """The object permission manager"""

    def update_or_create(self, permission, owner_object, target_object):
        """
        Update or create an object permission from owner and target objects.
        """
        owner_content_type = ContentType.objects.get_for_model(owner_object)
        target_content_type = ContentType.objects.get_for_model(target_object)

        return super().update_or_create(
            permission=permission,
            owner_object_id=str(owner_object.pk),
            owner_content_type=owner_content_type,
            target_object_id=str(target_object.pk),
            target_content_type=target_content_type,
        )


class ObjectPermission(models.Model):
    """The object permission model"""

    permission = models.ForeignKey("auth.Permission", on_delete=models.CASCADE)
    owner_object_id = models.CharField(max_length=255)  # Store any ID as a string
    owner_content_type = models.ForeignKey("contenttypes.ContentType", on_delete=models.CASCADE, related_name="owner_object")
    target_object_id = models.CharField(max_length=255)  # Store any ID as a string
    target_content_type = models.ForeignKey("contenttypes.ContentType", on_delete=models.CASCADE, related_name="target_object")

    objects = ObjectPermissionManager()

    def get_owner_object(self):
        """
        Get the object for the permission
        """
        try:
            content_type = self.owner_content_type.model_class()
            return content_type.objects.get(id=self.owner_object_id)
        except (ValueError, content_type.DoesNotExist):
            return None

    def get_target_object(self):
        """
        Get the object for the permission
        """
        try:
            content_type = self.target_content_type.model_class()
            return content_type.objects.get(id=self.target_object_id)
        except (ValueError, content_type.DoesNotExist):
            return None

    def __str__(self):
        return self.owner_object_id


class APIKeyClient(models.Model):
    """The API key client model"""

    email = models.EmailField(primary_key=True)
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def has_perm(self, perm, obj=None):
        """
        Check if the client has a specific permission on the target object.
        """
        if obj is None:
            # Global permission check
            return False

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
        Return a set of permission strings that the client has.
        """
        permissions = ObjectPermission.objects.filter(
            owner_object_id=str(self.pk),
            owner_content_type=ContentType.objects.get_for_model(self),
        ).values_list("permission__codename", "target_object_id", "target_content_type")

        return permissions

    def __str__(self):
        return self.name


class APIKey(models.Model):
    """The API key model"""

    key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    client = models.OneToOneField(APIKeyClient, on_delete=models.CASCADE, related_name="api_key")

    def __str__(self):
        return self.key


class Session(models.Model):
    """The session model"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ip = models.GenericIPAddressField(unique=True)
    user_agent = models.CharField(max_length=255, blank=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    time_zone = models.CharField(max_length=255, blank=True)
    asn = models.CharField(max_length=255, blank=True)
    a_s = models.CharField(max_length=255, blank=True)
    is_proxy = models.BooleanField(default=False)
    is_vpn = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    country = models.ForeignKey("geo.Country", on_delete=models.CASCADE, blank=True, null=True)
    administrative_level_primary = models.ForeignKey("geo.AdministrativeLevelPrimary", on_delete=models.CASCADE, blank=True, null=True)
    administrative_level_secondary = models.ForeignKey("geo.AdministrativeLevelSecondary", on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey("geo.City", on_delete=models.CASCADE, blank=True, null=True)
    token = models.ForeignKey(AuthToken, on_delete=models.CASCADE, blank=True, null=True)
    api_key = models.ForeignKey("auth_core.APIKey", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.key
