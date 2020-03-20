from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ..models.challenge import Challenge
from ..models.hero import Hero
from ..models.villain import Villain
from ..models.story_template import StoryTemplate
from ..models.story_setting import StorySetting


@login_required
def story_elements(request):
     if request.method == 'GET':
        users = User.objects.all()
        for user in users:
            print("**********************", user.hero_set.all())
        template = 'story_elements.html'
        context = {
            "users": users
        }

        return render(request, template, context)

    # if request.method == 'GET':

    #     for user in kids:
    #         for storyprompt in kid.storyprompt_set.all():
    #             print(storyprompt) # This prints the story prompts in the terminal.
    #         # print("********************", kid.storyprompt_set.all() ) # _set is a Django reserved ORM method to get an array of items with this object's foreign key from another table.
    #     template = 'home.html'
    #     context = {
    #         "kids": kids
    #     }

    #     return render(request, template, context)

