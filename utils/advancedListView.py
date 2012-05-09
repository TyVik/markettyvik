#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from functools import update_wrapper
from django.views.generic.edit import DeletionMixin, ModelFormMixin
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import ListView
from django.utils.decorators import classonlymethod

class AdvancedListView(ListView, ModelFormMixin, DeletionMixin):
    pk_url_kwarg = 'id'

    @classonlymethod
    def as_delete(cls, **initkwargs):
        def view(request, *args, **kwargs):
            self = cls(**initkwargs)
            if hasattr(self, 'get') and not hasattr(self, 'head'):
                self.head = self.get
            self.request = request
            self.args = args
            self.kwargs = kwargs
            return self.delete(self.request)
        update_wrapper(view, cls, updated=())
        update_wrapper(view, cls.dispatch, assigned=())
        return view

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        list_context = ListView.get_context_data(self, object_list=self.object_list)
        self.object = None
        context = ModelFormMixin.get_context_data(self, form=self.get_form(self.get_form_class()))
        context.update(list_context)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    # PUT is a valid HTTP verb for creating (with a known URL) or editing an
    # object, note that browsers only support POST for now.
    def put(self, *args, **kwargs):
        return self.post(*args, **kwargs)

