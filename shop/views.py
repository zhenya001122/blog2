from django.shortcuts import render

from shop.models import Product


def shop_product(request):
    products = Product.objects.all()
    return render(request, 'shop/shop_list.html', {'products': products})