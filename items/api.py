# coding: utf-8
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication

from models import Items


class ItemsResource(ModelResource):
    class Meta:
        queryset = Items.objects.all()
        resource_name = 'items'
        allowed_methods = ['post', 'get', 'patch', 'delete']
        authentication = Authentication()
        authorization = Authorization()
        always_return_data = True
