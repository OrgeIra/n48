# home/views.py
from django.shortcuts import render


from products.models import Category

def home_view(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})


def detail(request):
    return render(request, 'detail.html')
