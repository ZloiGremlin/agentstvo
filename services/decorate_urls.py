#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import Decorates


urlpatterns = patterns('',
    url(r'^$', Decorates.as_view(), name='decor_list'),
)