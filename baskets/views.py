from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView, UpdateView

from baskets.models import Basket

from mainapp.models import Product




# @login_required
# def add_product(request, id):
#     user_select = request.user
#     product = Product.objects.get(id=id)
#     baskets = Basket.objects.filter(user=user_select, product=product)
#
#     if baskets:
#             baskets = baskets.first()
#             baskets.quantity += 1
#             baskets.save()
#     else:
#             Basket.objects.create(user=user_select, product=product, quantity=1)
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def add_product(request, id):
    if request.is_ajax():
        user_select = request.user
        product = Product.objects.get(id=id)
        baskets = Basket.objects.filter(user=user_select, product=product)

        if baskets:
                baskets = baskets.first()
                baskets.quantity += F('quantity') + 1
                baskets.save()
        else:
                Basket.objects.create(user=user_select, product=product, quantity=1)
    result = render_to_string('mainapp/Cards.html')
    return JsonResponse({'result': result})



class DeleteProduct(DeleteView):
    model = Basket
    template_name = 'baskets/basket.html'
    success_url = reverse_lazy('index')
    context_object_name = 'basket'


    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(DeleteProduct, self).dispatch(request, *args, **kwargs)


@login_required
def edit_basket(request, id_basket, quantity):
    if request.is_ajax():
        basket = Basket.objects.get(id=id_basket)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()

        baskets = Basket.objects.filter(user=request.user)

        context = {
            'baskets' : baskets
        }
        result = render_to_string('baskets/basket.html', context)
        return JsonResponse({'result': result})


