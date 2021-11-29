from django.urls import path

from authapp.views import login, register, logout, profile
from baskets.views import add_product, delete_product

app_name='baskets'
urlpatterns = [

    path('add/<int:id>/', add_product, name='add_product'),
    path('remove/<int:basket_id>/', delete_product, name='delete_product'),

]