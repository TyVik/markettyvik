# coding: utf-8

from django.conf.urls.defaults import patterns, url
from views import FormAndListView, delete
from models import Items
from forms import ItemsForm
from django.core.urlresolvers import reverse_lazy


urlpatterns = patterns('',
    url(r'^$', FormAndListView.as_view(
        queryset=Items.objects.all(),
        context_object_name='itemsProd',
        form_class=ItemsForm,
        success_url=reverse_lazy('items:index'),
        template_name='items/items.html',
    ), name="index"),
    url(r'delete/(?P<pk>\d+)', delete)
)
