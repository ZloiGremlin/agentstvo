#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import Cakes


urlpatterns = patterns('',
    url(r'^$', Cakes.as_view(), name='cake_list'),
)