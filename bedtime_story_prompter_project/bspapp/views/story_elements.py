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
def story_elements(request, hero_id=None, villain_id=None, setting_id=None, challenge_id=None, template_id=None):
    if request.method == 'GET':
        user = User.objects.get(pk=request.user.id)
        template = 'story_elements.html'
        context = {
            "user": user
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        user = User.objects.get(pk=request.user.id)

        if ("actual_method" in form_data and form_data["actual_method"] == "DELETE") and hero_id is not None:
            hero = Hero.objects.get(pk=hero_id)
            hero.delete()
            return redirect(reverse('story_elements'))

        if ("actual_method" in form_data and form_data["actual_method"] == "PUT") and hero_id is not None:
            print("----------------FORM DATA AFTER CLICKING UPDATE", form_data)
            hero = Hero.objects.get(pk=hero_id)
            hero.name = form_data["hero"]
            hero.save()
            return redirect(reverse('story_elements'))

        if ("actual_method" in form_data and form_data["actual_method"] == "DELETE") and villain_id is not None:
            villain = Villain.objects.get(pk=villain_id)
            villain.delete()
            return redirect(reverse('story_elements'))

        if ("actual_method" in form_data and form_data["actual_method"] == "DELETE") and setting_id is not None:
            setting = StorySetting.objects.get(pk=setting_id)
            setting.delete()
            return redirect(reverse('story_elements'))

        if ("actual_method" in form_data and form_data["actual_method"] == "DELETE") and challenge_id is not None:
            challenge = Challenge.objects.get(pk=challenge_id)
            challenge.delete()
            return redirect(reverse('story_elements'))

        if ("actual_method" in form_data and form_data["actual_method"] == "DELETE") and template_id is not None:
            template = StoryTemplate.objects.get(pk=template_id)
            template.delete()
            return redirect(reverse('story_elements'))

        else:
            try:
                new_hero = Hero(
                    name = form_data["hero"],
                    user = user
                )
                new_hero.save()

            except:
                try:
                    new_villain = Villain(
                        name = form_data["villain"],
                        user = user
                    )
                    new_villain.save()

                except:
                    try:
                        new_setting = StorySetting(
                            description = form_data["setting"],
                            user = user
                        )
                        new_setting.save()

                    except:
                        try:
                            new_challenge = Challenge(
                                description = form_data["challenge"],
                                user = user
                            )
                            new_challenge.save()

                        except:
                            new_template = StoryTemplate(
                                template = form_data["template"],
                                user = user
                            )
                            new_template.save()


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

