from django.db import models
from django.conf import settings


class BirthdayReminder(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='birthdays'
    )

    name = models.CharField(max_length=100)
    dob = models.DateField()
    notes = models.TextField(blank=True, null=True)

    reminder_time = models.TimeField(default="09:00:00")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.dob})"