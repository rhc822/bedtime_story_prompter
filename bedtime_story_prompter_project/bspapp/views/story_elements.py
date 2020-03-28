from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Permission
from django.shortcuts import reverse, redirect
from ..models.challenge import Challenge
from ..models.hero import Hero
from ..models.villain import Villain
from ..models.story_template import StoryTemplate
from ..models.story_setting import StorySetting


################################################################
# WHEN A USER CLICKS THE 'STORY ELEMENTS' BUTTON IN THE NAVBAR, A URL REQUEST IS MADE FOR 'storyelements/' AND THE 'story_elements' FUNCTION IS CALLED INITIALLY WITH A 'GET' REQUEST FOR THE USER OBJECT USING THE ORM. WHEN A 'POST' CALL IS MADE, THE REQUEST GOES THROUGH A SERIES OF CONDITIONS TO DETERMINE WHERE THE REQUEST NEEDS TO BE ROUTED, WHETHER THE 'POST' REQUEST IS ACTUALLY A 'PUT', A 'DELETE', OR ELSE WHETHER IT'S CREATING A NEW ITEM (.SAVE).
################################################################

@login_required
def story_elements(request, hero_id=None, villain_id=None, setting_id=None, challenge_id=None, template_id=None): # These parameters are necessary in the 'POST' section and must be set to None to avoid the GET request thinking it needs to use them in some way.
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

        # Since a browser can only POST or GET, I used the hidden input to send the actual method (of a DELETE or PUT). I then compared the value of the story element id that was also sent in the same request to the value of None (originally set as a parameter at the beginning of the function call).

        if ("actual_method" in form_data and form_data["actual_method"] == "DELETE") and hero_id is not None:
            hero = Hero.objects.get(pk=hero_id)
            hero.delete()
            return redirect(reverse('story_elements'))

        if ("actual_method" in form_data and form_data["actual_method"] == "PUT") and hero_id is not None:
            hero = Hero.objects.get(pk=hero_id)
            hero.name = form_data["hero"]
            hero.save()
            return redirect(reverse('story_elements'))

        if ("actual_method" in form_data and form_data["actual_method"] == "DELETE") and villain_id is not None:
            villain = Villain.objects.get(pk=villain_id)
            villain.delete()
            return redirect(reverse('story_elements'))

        if ("actual_method" in form_data and form_data["actual_method"] == "PUT") and villain_id is not None:
            villain = Villain.objects.get(pk=villain_id)
            villain.name = form_data["villain"]
            villain.save()
            return redirect(reverse('story_elements'))

        if ("actual_method" in form_data and form_data["actual_method"] == "DELETE") and setting_id is not None:
            setting = StorySetting.objects.get(pk=setting_id)
            setting.delete()
            return redirect(reverse('story_elements'))

        if ("actual_method" in form_data and form_data["actual_method"] == "PUT") and setting_id is not None:
            setting = StorySetting.objects.get(pk=setting_id)
            setting.description = form_data["setting"]
            setting.save()
            return redirect(reverse('story_elements'))

        if ("actual_method" in form_data and form_data["actual_method"] == "DELETE") and challenge_id is not None:
            challenge = Challenge.objects.get(pk=challenge_id)
            challenge.delete()
            return redirect(reverse('story_elements'))

        if ("actual_method" in form_data and form_data["actual_method"] == "PUT") and challenge_id is not None:
            challenge = Challenge.objects.get(pk=challenge_id)
            challenge.description = form_data["challenge"]
            challenge.save()
            return redirect(reverse('story_elements'))

        if ("actual_method" in form_data and form_data["actual_method"] == "DELETE") and template_id is not None:
            template = StoryTemplate.objects.get(pk=template_id)
            template.delete()
            return redirect(reverse('story_elements'))

        if ("actual_method" in form_data and form_data["actual_method"] == "PUT") and template_id is not None:
            template = StoryTemplate.objects.get(pk=template_id)
            template.template = form_data["template"]
            template.save()
            return redirect(reverse('story_elements'))

        # If the above conditions don't execute, the code then goes through a sequence of 'try' and 'excepts' that form the "create" portion of the condition list.

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