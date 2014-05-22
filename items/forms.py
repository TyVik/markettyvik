# coding: utf-8
from django.forms import ModelForm

from models import Items

class ItemsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ItemsForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs["class"] = "input-sm"

    class Meta:
        model = Items