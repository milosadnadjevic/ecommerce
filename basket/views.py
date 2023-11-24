from django.shortcuts import render

def basket_summary(request):
    return render(request, 'ecommerce/basket/summary.html')
