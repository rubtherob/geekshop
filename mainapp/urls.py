from django.urls import path
from mainapp.views import products, detail

app_name='products'
urlpatterns = [

    path('', products, name='products'),
    path('detail/<int:pk>', detail, name='detail')
]