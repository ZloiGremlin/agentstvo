#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import ArtistList


urlpatterns = patterns('',
    url(r'^$', ArtistList.as_view(type_artist='mc'), name='mc_list'),
)