from django.urls import path


from baskets.views import add_product, DeleteProduct, edit_basket

app_name='baskets'
urlpatterns = [

    path('add/<int:id>/', add_product, name='add_product'),
    path('remove/<int:pk>/', DeleteProduct.as_view(), name='delete_product'),
    path('edit/<int:id_basket>/<int:quantity>/', edit_basket, name='edit_basket'),

]