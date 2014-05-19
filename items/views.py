# coding: utf-8

from models import Items
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from decorators import ajax_required
from django.views.generic import ListView


class FormAndListView(ListView):

    form_class = None
    success_url = None

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(self.success_url)


@ajax_required
def delete(request, pk):
    item = get_object_or_404(Items, pk=pk)
    item.delete()
    return HttpResponse("ok")