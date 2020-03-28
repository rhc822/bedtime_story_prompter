from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from ..models.kid import Kid


################################################################
# WHEN A USER FIRST LOGS IN AND/OR CLICKS THE 'STORIES' BUTTON IN THE NAVBAR, A URL REQUEST IS MADE FOR '', AND THE home FUNCTION IS CALLED GETTING A LIST OF ALL KIDS UNDER THE USERS' ID.
################################################################

@login_required
def home(request):
    if request.method == 'GET':
        user = User.objects.get(pk=request.user.id)
        kids = Kid.objects.filter(user_id=user.id)
        template = 'home.html'
        context = {
            "kids": kids
        }

        return render(request, template, context)

