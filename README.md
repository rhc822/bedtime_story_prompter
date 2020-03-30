# Bedtime Story Prompter

![image](https://user-images.githubusercontent.com/54753720/77921286-2ec2c080-7265-11ea-8c79-eb26d3b53db5.png)

This app enables users to create a profile, add a child, generate a random story, and save it to the child's list. The story prompts are created from randomly-selected items in a few pre-set categories. Users can add, edit, and delete items in these story elements categories. The templates with which the prompt pulls from also have these capabilities. Before saving, users have the final say to adjust the story prompt how they see fit.

## Background

I put my two small kids down to sleep every night and love telling them stories. They almost always tell me elements to include in the story (e.g. hero, villain, setting, and so on). I tend to get the same story elements, and I want to spice up story time, so I decided to let technology help with that.

## Set up 

1. Ensure you have the [Python](https://www.python.org/downloads/) programming language installed on your system
1. Ensure you have [Django](https://docs.djangoproject.com/en/3.0/intro/install/) web framework installed on your system 

## Using the app

1. Clone this repository
1. In your command line, `cd` into the directory it creates and navigate into `bedtime_story_prompter_project` (the directory where `manage.py` is located)
1. Run `python manage.py runserver`
1. In your browser, navigate to the localhost address provided by the server (e.g. http://127.0.0.1:8000/)
1. If you are a new user, select the __Register__ option
1. If you are a returning user, select the __Login__ option
1. Either:
   1. Choose a story to tell from the selected list or
   1. Click __Create New Story__ to generate a new random story prompt
1. To add story element items, click __Story Elements__


Happy story telling!
