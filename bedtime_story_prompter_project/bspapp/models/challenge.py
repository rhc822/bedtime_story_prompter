from django.db import models
from django.contrib.auth.models import User


class Challenge(models.Model):

    description = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)