from django.db import models
from django.contrib.auth.models import User
from .kid import Kid


class StoryPrompt(models.Model):

    text = models.CharField(max_length=1000)
    kid = models.ForeignKey(Kid, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
