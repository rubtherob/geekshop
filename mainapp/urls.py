from django.urls import path
from mainapp.views import Detail, ProductView

app_name='products'
urlpatterns = [

    path('', ProductView.as_view(), name='products'),
    path('category/<int:id_category>', ProductView.as_view(), name='category'),
    path('detail/<int:pk>', Detail.as_view(), name='detail')
]