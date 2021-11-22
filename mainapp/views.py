
from django.shortcuts import render
from .models import ProductCategory, Product




def index(request):
    context = {
        'title': 'geekbrains',

    }
    return render(request, 'mainapp/index.html', context)



def products(request):
    context = {
        'title': 'geekbrains - каталог',
        'products': Product.objects.all()
    }
    return render(request, 'mainapp/products.html', context)
