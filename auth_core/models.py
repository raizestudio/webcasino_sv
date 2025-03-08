from django.db import models
from uuid import UUID


class ObjectPermission(models.Model):
    """The object permission model"""
    permission = models.ForeignKey("auth.Permission", on_delete=models.CASCADE)
    owner_object_id = models.CharField(max_length=255)  # Store any ID as a string
    owner_content_type = models.ForeignKey("contenttypes.ContentType", on_delete=models.CASCADE, related_name="owner_object")
    target_object_id = models.CharField(max_length=255)  # Store any ID as a string
    target_content_type = models.ForeignKey("contenttypes.ContentType", on_delete=models.CASCADE, related_name="target_object")
    
 

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
        return self.permission.name
    
class APIKeyClient(models.Model):
    """The API key client model"""
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class APIKey(models.Model):
    """The API key model"""
    key = models.CharField(max_length=128, primary_key=True)
    label = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    client = models.ForeignKey(APIKeyClient, on_delete=models.CASCADE, related_name="api_key")

    def __str__(self):
        return self.key