from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


def is_discord_webhook(webhook: str):

    def startswith(pattern: str, _with: str):
        return pattern.startswith(_with)

    if not any([
        startswith(webhook, 'https://discord.com/api/webhooks'),
        startswith(webhook, 'discord.com/api/webhooks'),
    ]):
        raise ValidationError("WEBHOOK is starts with ")


class Customer(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    webhook = models.TextField(validators=[is_discord_webhook])

