# coding: utf-8

from models import Items
from markettyvik.utils.advancedListView import AdvancedListView

class ItemsView(AdvancedListView):
    model = Items
    context_object_name = 'itemsProd'
    template_name = 'index.html'
    success_url = '/items/index/'

    def get_queryset(self):
        return Items.objects.all()
