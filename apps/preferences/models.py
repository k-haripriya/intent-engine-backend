from django.db import models
from django.conf import settings

class UserPreference(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    theme = models.CharField(max_length=20, default="light")
    language = models.CharField(max_length=20, default="en")

    def __str__(self):
        return f"{self.user.username} preferences"