from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ..models.kid import Kid
from ..models.challenge import Challenge
from ..models.hero import Hero
from ..models.villain import Villain
from ..models.story_template import StoryTemplate
from ..models.story_setting import StorySetting


@login_required
def create_new_story(request):
     if request.method == 'GET':
        template = StoryTemplate.objects.all()
        print(template)
        # kids = Kid.objects.all()
        # users = User.objects.all()

        template = 'create_new_story.html'
        context = {
            "users": users,
            "kids": kids
        }

        return render(request, template, context)
