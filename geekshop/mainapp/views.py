
from django.shortcuts import render
import json
import os

with open(os.path.abspath('mainapp/fixtures/prod.json'),'r',encoding='utf-8') as f:
    products_with_json = json.load(f)

print(products_with_json)

def index(request):
    context = {
        'title': 'geekbrains',

    }
    return render(request, 'mainapp/index.html', context)



def products(request):
    context = {
        'title': 'geekbrains - каталог',
        'products': products_with_json
    }
    return render(request, 'mainapp/products.html', context)
