from django.db import models


class Message(models.Model):
    content = models.TextField()

    author = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Room(models.Model):
    name = models.CharField(max_length=100)

    messages = models.ManyToManyField(Message, blank=True)

    def __str__(self):
        return self.name
