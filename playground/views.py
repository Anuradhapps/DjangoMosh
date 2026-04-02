from django.shortcuts import render
from store.models import Product


def say_hello(request):
    product = Product.objects.filter(unit_price__gt=450)

    return render(request, "hello.html", {"product": product})
