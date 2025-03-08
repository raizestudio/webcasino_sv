from django.db import models

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