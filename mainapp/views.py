from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Product, ProductCategory
from django.conf import settings
from django.core.cache import cache


def get_link_category():
    if settings.LOW_CACHE:
        key = 'link_category'
        link_category = cache.get(key)
        if link_category is None:
            link_category = ProductCategory.objects.all()
            cache.set(key,link_category)
        return link_category
    else:
        return ProductCategory.objects.all()
# Create your views here.


def get_link_product():
    if settings.LOW_CACHE:
        key = 'link_product'
        link_product = cache.get(key)
        if link_product is None:
            link_product = Product.objects.all().select_related('category')
            cache.set(key,link_product)
        return link_product
    else:
        return Product.objects.all().select_related('category')


def get_product(pk):
    if settings.LOW_CACHE:
        key = f'product{pk}'
        product = cache.get(key)
        if product is None:
            product = Product.objects.get(id=pk)
            cache.set(key,product)
        return product
    else:
        return Product.objects.get(id=pk)



def index(request):
    context = {
        'title': 'geekbrains',

    }
    return render(request, 'mainapp/index.html', context)



class Detail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'mainapp/detail.html'



class ProductView(ListView):
    paginate_by = 3
    model = Product
    context_object_name = 'product'
    template_name = 'mainapp/products.html'

    def get_queryset(self, **kwargs):
        if self.kwargs:
            return Product.objects.filter(category_id=self.kwargs['id_category'])
        return Product.objects.all().order_by('id')

    
    def get_context_data(self, *, object_list=None, **kwargs):
       context = super(ProductView, self).get_context_data(**kwargs)
       context['title'] = 'geekbrains - каталог'
       context['categories'] = get_link_category()
       return context