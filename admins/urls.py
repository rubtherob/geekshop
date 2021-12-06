from django.urls import path

from admins.views import index, read_users, create_user, edit_user, delete_user, read_product_category, \
    create_product_category, edit_category, delete_category, read_products, create_product, edit_product, delete_product

app_name='admins'
urlpatterns = [

    path('', index, name='index'),

    path('users/', read_users, name='users'),
    path('create_user/', create_user, name='create_user'),
    path('edit_user/<int:pk>', edit_user, name='edit_user'),
    path('delete_user/<int:pk>', delete_user, name='delete_user'),

    path('categories/', read_product_category, name='categories'),
    path('create_category/', create_product_category, name='create_category'),
    path('edit_category/<int:pk>', edit_category, name='edit_category'),
    path('delete_category/<int:pk>', delete_category, name='delete_category'),

    path('products/', read_products, name='products'),
    path('create_product/', create_product, name='create_product'),
    path('edit_product/<int:pk>', edit_product, name='edit_product'),
    path('delete_product/<int:pk>', delete_product, name='delete_product'),

]