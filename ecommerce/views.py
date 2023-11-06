from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def categories(request):
    return {
        'categories': Category.objects.all()
    }


def all_products(request):
    products = Product.objects.all()
    return render(request, 'ecommerce/home.html', {'products': products})

def product_detail (request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'products/detail.html', {'product': product})
