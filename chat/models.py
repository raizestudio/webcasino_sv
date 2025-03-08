from django.db import models


class Message(models.Model):
    """Model definition for Message."""
    content = models.TextField()

    author = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Room(models.Model):
    """Model definition for Room."""
    name = models.CharField(max_length=100)
    is_public = models.BooleanField(default=True)

    messages = models.ManyToManyField(Message, blank=True)

    def __str__(self):
        return self.name
