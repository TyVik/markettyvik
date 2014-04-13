# coding: utf-8

from models import Items
from utils.advancedListView import AdvancedListView

class ItemsView(AdvancedListView):
    model = Items
    context_object_name = 'itemsProd'
    template_name = 'items.html'
    success_url = '/items/'

    def get_queryset(self):
        return Items.objects.all()
