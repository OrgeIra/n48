# home/views.py
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def detail(request):
    return render(request, 'detail.html')