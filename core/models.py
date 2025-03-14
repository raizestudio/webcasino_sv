from django.db import models


class Menu(models.Model):
    """The menu model"""

    name = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    target = models.CharField(max_length=100)  # Used to identify position client side
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="children",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"

    def __str__(self):
        return self.name


class ApiProvider(models.Model):
    """The API provider model"""

    name = models.CharField(max_length=100)
    base_url = models.URLField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["name"]
        verbose_name = "API Provider"
        verbose_name_plural = "API Providers"

    def __str__(self):
        return self.name
