from django.db import models
import uuid


class ScraperModel(models.Model):
    token = models.UUIDField(default=uuid.uuid4)
    start_time = models.TimeField(default=None, blank=True, null=True)
    end_time = models.TimeField(default=None, blank=True, null=True)
    name = models.TextField(default=None, blank=True, null=True)
    can_work = models.BooleanField(default=False)
