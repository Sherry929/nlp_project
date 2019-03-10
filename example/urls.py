# -*- coding: UTF-8 -*-

from django.conf.urls import url
from example.views import chat


app_name = 'example'
urlpatterns = [
    url(r'^$', chat, name='chat'),
]