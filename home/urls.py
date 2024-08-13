from django.urls import path
from .views import home_view, detail

urlpatterns = [
    path('', home_view, name='home_view'),
    path('detail/', detail, name='detail'),
    
]
