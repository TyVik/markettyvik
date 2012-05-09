# coding: utf-8

from django.conf.urls.defaults import patterns, url, include
from views import ItemsView

urlpatterns = patterns('',
    url(r'index/$', ItemsView.as_view()),
    url(r'delete/(?P<id>\d*)/$', ItemsView.as_delete()),
)
