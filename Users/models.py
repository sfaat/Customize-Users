from django.db import models


class Role(TimeStampedModel):
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name