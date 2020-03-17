from django.db import models
from django.contrib.auth.models import User
from .kid import Kid

# Note how this is different from the original Libray app Librarian Model. No post_save stuff going on. Since we want to use some of the form data to create a Librarian when a new user registers, we will handle making a librarian in the register view.
class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # kid = models.ForeignKey(
    #     Kid, related_name="kids",
    #     null=True, # Makes column nullable in DB
    #     blank=True, # Allows blank value on objects
    #     on_delete=models.CASCADE)
    kid_first_name = models.CharField(max_length=50)

