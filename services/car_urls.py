#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import ArtistList, CarList


urlpatterns = patterns('',
    url(r'^$', CarList.as_view(), name='car_list'),
)