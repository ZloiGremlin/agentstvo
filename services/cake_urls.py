#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import Cakes, CategoryCakes


urlpatterns = patterns('',
    url(r'^$', CategoryCakes.as_view(), name='cake_category'),
    url(r'^(?P<slug>[0-9A-Za-z-_.//]+)/$', Cakes.as_view(), name='cake_list'),
)