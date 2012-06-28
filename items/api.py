# coding: utf-8

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import django
from models import Items

def list(request):
    items = Items.objects.values('id', 'name')
    result = ''
    for item in items:
        result += str(item['id']) + '^' + item['name'] + '$'
    return HttpResponse(result[:-1])

def delete(request, id):
    Items.objects.filter(id=id).delete()
    return HttpResponse('')

@csrf_exempt
def add(request):
    result = HttpResponse(400)
    if request.method == 'POST':
        print request.POST
        item = Items()
        item.name = request.POST['name']
        item.save()
        result = HttpResponse('')
    return result

def help(request):
    help = """
<h1>API для доступа к списку покупок</h1>
<ul>
<li>list - получить список продуктов</li>
<li>delete - удалить продукт</li>
<li>add - добавить продукт</li>
<ul>
"""
    return HttpResponse(help)