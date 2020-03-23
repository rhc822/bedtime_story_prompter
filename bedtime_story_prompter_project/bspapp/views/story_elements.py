from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Permission
from django.shortcuts import reverse, redirect
from ..models.challenge import Challenge
from ..models.hero import Hero
from ..models.villain import Villain
from ..models.story_template import StoryTemplate
from ..models.story_setting import StorySetting


@login_required
def story_elements(request):
    if request.method == 'GET':
        user = User.objects.get(pk=request.user.id)
        # print(user.hero_set.all())
        # for user in users:
        #     print("**********************", user.hero_set.all())
        template = 'story_elements.html'
        context = {
            "user": user
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        user = User.objects.get(pk=request.user.id)
        # kid = Kid.objects.filter(user_id=user.id)
        new_hero = Hero(
            name = form_data["hero"],
            user = user
        )
        new_hero.save()


        return redirect(reverse('story_elements'))


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

