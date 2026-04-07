from django.shortcuts import render
from store.models import Product, OrderItem, Order
from django.db.models.aggregates import Count, Min, Max, Avg, Sum
from django.db.models import Q, F, Value


def say_hello(request):

    querryset = Product.objects.annotate(isnew=Value(True))
    return render(request, "hello.html", {"products": list(querryset)})
