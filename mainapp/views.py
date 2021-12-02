
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

def detail(request,pk):
    context = {
        'title': 'geekbrains - детали',
        'product': Product.objects.get(id=pk)
    }
    return render(request, 'mainapp/detail.html', context)
