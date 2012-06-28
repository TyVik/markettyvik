# coding: utf-8

from django.conf.urls.defaults import patterns, url, include
from views import ItemsView
import api

urlpatterns = patterns('',
    url(r'^$', ItemsView.as_view()),
    url(r'delete/(?P<pk>\d*)/$', ItemsView.as_delete()),

    url(r'api/list$', api.list),
    url(r'api/add$', api.add),
    url(r'api/delete/(\d*)$', api.delete),
    url(r'api/$', api.help)
)
