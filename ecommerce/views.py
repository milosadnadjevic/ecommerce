from django.shortcuts import render
from .models import Product, Category

def categories(request):
    return {
        'categories': Category.objects.all()
    }


def all_products(request):
    products = Product.objects.all()
    return render(request, 'ecommerce/home.html', {'products': products})