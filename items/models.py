#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.db import models
from django.contrib import admin

class Items(models.Model):
    name = models.CharField(max_length=128, verbose_name=u'')

    def __unicode__(self):
        return self.name

    class Meta(object):
        db_table = 'items'

class ItemsAdmin(admin.ModelAdmin):
    list_display = ('name',)
