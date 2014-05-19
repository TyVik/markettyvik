#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView
from tastypie.api import Api
from items.api import ItemsResource


v1_api = Api(api_name='v1')
v1_api.register(ItemsResource())

urlpatterns = patterns('',
    url(r'^items/', include('items.urls', namespace="items")),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    (r'^api/', include(v1_api.urls)),
)
