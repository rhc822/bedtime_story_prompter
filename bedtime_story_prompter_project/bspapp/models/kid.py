from django.db import models
from django.contrib.auth.models import User


class Kid(models.Model):

    kid_first_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)