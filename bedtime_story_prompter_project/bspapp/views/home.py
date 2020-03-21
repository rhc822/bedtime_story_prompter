from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from ..models.kid import Kid

@login_required
def home(request):
    if request.method == 'GET':
        user = User.objects.get(pk=request.user.id)
        kids = Kid.objects.filter(user_id=user.id)
        for kid in kids:
            for storyprompt in kid.storyprompt_set.all():
                print(storyprompt) # This prints the story prompts in the terminal.
            # print("********************", kid.storyprompt_set.all() ) # _set is a Django reserved ORM method to get an array of items with this object's foreign key from another table.
        template = 'home.html'
        context = {
            "kids": kids
        }

        return render(request, template, context)

