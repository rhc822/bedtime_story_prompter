from django.db import models
from .parent import Parent


class Kid(models.Model):

    kid_first_name = models.CharField(max_length=50)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)