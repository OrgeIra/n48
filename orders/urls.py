from django.urls import path
from .views import order_list, order_detail
from .views import create_order


urlpatterns = [
    path('', order_list, name='order_list'),
    path('<int:pk>/', order_detail, name='order_detail'),
    path('create/', create_order, name='create_order'),
    
]


