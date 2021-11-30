from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from baskets.models import Basket
from mainapp.models import Product




@login_required
def add_product(request, id):
    user_select = request.user
    product = Product.objects.get(id=id)
    baskets = Basket.objects.filter(user=user_select,product=product)

    if baskets:
            baskets = baskets.first()
            baskets.quantity += 1
            baskets.save()
    else:
            Basket.objects.create(user=user_select,product=product,quantity=1)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def delete_product(request, basket_id):
    Basket.objects.get(id=basket_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))