from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.models import User
from ..models.kid import Kid


################################################################
# BEFORE LOGGING IN, WHEN A USER CLICKS THE 'REGISTER' BUTTON IN THE NAVBAR, A URL REQUEST IS MADE FOR 'register/' AND THE 'register_user' FUNCTION IS CALLED INITIALLY ONLY DISPLAYING THE REGISTER TEMPLATE. WHEN A 'POST' CALL IS MADE, A USER (PARENT) INSTANCE IS CREATED, A KID INSTANCE IS CREATED, AND THE USER IS LOGGED IN.
################################################################

def register_user(request):
    """View method for handling creation of a new user for auth
        Args:
        request = full http object
    """

    # For handling when user submits the form data
    if request.method == "POST":

        # First create a new user using django's built in craziness. create_user is a method in django.
        new_user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )

        # Second, make a kid after the user has been created
        kid = Kid.objects.create(
            user=new_user,
            # This is other form data to save on the new user (parent) that isn't a property of the User model...
            kid_first_name=request.POST['kid_first_name']
        )

        login(request, new_user)

        # Redirect the browser to wherever you want to go after registering
        return redirect(reverse('home'))

    # handles a request to load the empty form for the useer to fill out
    else:
        template = 'register.html'

    return render(request, template, {})