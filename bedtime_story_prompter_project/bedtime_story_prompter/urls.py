"""bedtime_story_prompter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from bspapp.views import *


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('register/', register_user, name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('create_new_story/', create_new_story, name='create_new_story'),
    # The 'normal' story element url for simply getting the elements
    path('storyelements/', story_elements, name='story_elements'),
    # The following are story element urls for deleting and editing various story elements
    path('storyelements/hero/<int:hero_id>', story_elements, name='hero_element'),
    path('storyelements/villain/<int:villain_id>', story_elements, name='villain_element'),
    path('storyelements/setting/<int:setting_id>', story_elements, name='setting_element'),
    path('storyelements/challenge/<int:challenge_id>', story_elements, name='challenge_element'),
    path('storyelements/template/<int:template_id>', story_elements, name='template_element')

]
