from django.shortcuts import render

from store.models import Product
from .models import *

# Create your views here.

def store(request):
    products = Product.objects.all()
    return render(request, 'store.html', {'products': products})

def cart(request):
    return render(request, 'cart.html', {})

def checkout(request):
    return render(request, 'checkout.html', {})

def base(request):
    return render(request, 'base.html', {})