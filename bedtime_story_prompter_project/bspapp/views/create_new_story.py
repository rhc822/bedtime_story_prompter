from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ..models.kid import Kid
from ..models.challenge import Challenge
from ..models.hero import Hero
from ..models.villain import Villain
from ..models.story_template import StoryTemplate
from ..models.story_setting import StorySetting
import random


@login_required
def create_new_story(request):
     if request.method == 'GET':
        user = User.objects.get(pk=request.user.id)
        kids = Kid.objects.filter(user_id=user.id)
        random_template = random.choice(StoryTemplate.objects.all())
        random_setting = random.choice(StorySetting.objects.all())
        random_villain = random.choice(Villain.objects.all())
        random_challenge = random.choice(Challenge.objects.all())
        random_hero = random.choice(Hero.objects.all())
        print("---------------\n", random_hero, "\n---------------")


        template = 'create_new_story.html'
        context = {
            "user": user,
            "kids": kids
        }

        return render(request, template, context)
