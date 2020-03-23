from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import reverse, redirect
from ..models.kid import Kid
from ..models.challenge import Challenge
from ..models.hero import Hero
from ..models.villain import Villain
from ..models.story_template import StoryTemplate
from ..models.story_setting import StorySetting
from ..models.story_prompt import StoryPrompt
import random


@login_required
def create_new_story(request):
    if request.method == 'GET':
        user = User.objects.get(pk=request.user.id)
        kids = Kid.objects.filter(user_id=user.id)
        random_template = str(random.choice(StoryTemplate.objects.filter(user_id=user.id)))
        random_setting = str(random.choice(StorySetting.objects.filter(user_id=user.id)))
        random_villain = str(random.choice(Villain.objects.filter(user_id=user.id)))
        random_challenge = str(random.choice(Challenge.objects.filter(user_id=user.id)))
        random_hero = str(random.choice(Hero.objects.filter(user_id=user.id)))
        print("\n**************\n", random_template, "\n**************")
        story_prompt = random_template.replace("[Hero]", random_hero)
        story_prompt = story_prompt.replace("[Villain]", random_villain)
        story_prompt = story_prompt.replace("[Challenge]", random_challenge)
        story_prompt = story_prompt.replace("[Setting]", random_setting)
        print("---------------\n", story_prompt, "\n---------------\n")

        template = 'create_new_story.html'
        context = {
            "user": user,
            "kids": kids[0],
            "story_prompt": story_prompt
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        user = User.objects.get(pk=request.user.id)
        kid = Kid.objects.filter(user_id=user.id)
        new_story_prompt = StoryPrompt(
            text = form_data["text"],
            kid = kid[0]
        )
        new_story_prompt.save()


        return redirect(reverse('home'))
