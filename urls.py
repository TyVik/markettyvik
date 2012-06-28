#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    url(r'^items/', include('markettyvik.items.urls')),
    url(r'^$', direct_to_template, {'template': 'index.html'})
#    url(r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'markettyvik.views.home', name='home'),
    # url(r'^markettyvik/', include('markettyvik.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
