from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Product, ProductCategory


def index(request):
    context = {
        'title': 'geekbrains',

    }
    return render(request, 'mainapp/index.html', context)



class Detail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'mainapp/detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
       context = super(Detail, self).get_context_data(**kwargs)
       context['title'] = 'geekbrains - продукт'
       return context


class ProductView(ListView):
    paginate_by = 3
    model = Product
    context_object_name = 'product'
    template_name = 'mainapp/products.html'

    def get_queryset(self, **kwargs):
        if self.kwargs:
            return Product.objects.filter(category_id=self.kwargs['id_category'])
        return Product.objects.all()

    
    def get_context_data(self, *, object_list=None, **kwargs):
       context = super(ProductView, self).get_context_data(**kwargs)
       context['title'] = 'geekbrains - каталог'
       context['categories'] = ProductCategory.objects.all()
       return context