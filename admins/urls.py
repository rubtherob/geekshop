from django.urls import path

from admins.views import index, ReadUsers, CreateUsers, EditUsers, DeleteUsers, ReadProductCategory, \
    CreateProductCategory, \
    EditCategory, DeleteCategory, ReadProduct, CreateProduct, EditProduct, DeleteProduct, ReadOrders, EditOrder

app_name='admins'



urlpatterns = [

    path('', index, name='index'),

    path('users/', ReadUsers.as_view(), name='users'),
    path('create_user/', CreateUsers.as_view(), name='create_user'),
    path('edit_user/<int:pk>', EditUsers.as_view(), name='edit_user'),
    path('delete_user/<int:pk>', DeleteUsers.as_view(), name='delete_user'),

    path('categories/', ReadProductCategory.as_view(), name='categories'),
    path('create_category/', CreateProductCategory.as_view(), name='create_category'),
    path('edit_category/<int:pk>', EditCategory.as_view(), name='edit_category'),
    path('delete_category/<int:pk>', DeleteCategory.as_view(), name='delete_category'),

    path('products/', ReadProduct.as_view(), name='products'),
    path('create_product/', CreateProduct.as_view(), name='create_product'),
    path('edit_product/<int:pk>', EditProduct.as_view(), name='edit_product'),
    path('delete_product/<int:pk>', DeleteProduct.as_view(), name='delete_product'),

    path('orders/<int:pk>', ReadOrders.as_view(), name='orders'),
    path('status/<int:pk>', EditOrder.as_view(), name='update_status'),

]