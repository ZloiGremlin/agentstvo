#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import Requisites


urlpatterns = patterns('',
    url(r'^$', Requisites.as_view(), name='req_list'),
)