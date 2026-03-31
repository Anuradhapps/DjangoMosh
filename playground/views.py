from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from store.models import Customer

def say_hello(request):
    try:
        customer = Customer.objects.get(pk=1400)
    except ObjectDoesNotExist:
        customer = None

    return render(request, 'hello.html',{
        'customer': customer.first_name if customer else None
    })


    return render(request, 'hello.html',{
        'customer': customer.first_name
    })
