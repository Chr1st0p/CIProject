"""CIProject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from MyApp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='home'),
    url(r"^keyworddetail/", views.mainstreamdetail),
    url(r"^socialdetail/", views.socialmediadetail),
    url(r"^getkeywords/", views.mainstream, name='getkeywords'),
    url(r"^mainstream/", views.mainstream, name='mainstream'),
    url(r"^socialmedia/", views.socialmedia, name='socialmedia'),
    url(r"^compare/", views.compare, name='compare'),
    url(r"^maindata/", views.mainstreamprocess, name='mainstreamkeywordjson'),
    url(r"^socialdata/", views.socialmediaprocess, name='socialmediakeywordjson'),
    url(r"^maincomparedata/", views.maincompareprocess, name='maincomparekeywordjson'),
    url(r"^socialcomparedata/", views.socialmediacompareprocess, name='socialmediacomparekeywordjson'),
    url(r"^mainsocicompare/", views.mainsocialcompareprocess, name='socialmediacomparekeywordjson'),
]
