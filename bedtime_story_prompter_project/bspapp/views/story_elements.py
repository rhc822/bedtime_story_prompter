from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models.challenge import Challenge
from ..models.hero import Hero
from ..models.villain import Villain
from ..models.story_template import StoryTemplate
from ..models.story_setting import StorySetting


@login_required
def story_elements(request):
     if request.method == 'GET':
        story_elements = user.objects.all()
        template = 'story_elements.html'
        context = {}

        print(story_elements)

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

