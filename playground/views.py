from django.shortcuts import render, get_object_or_404
from django.db import transaction
from store.models import Product, OrderItem, Order, Customer


def say_hello(request):
    with transaction.atomic():
        customer = get_object_or_404(Customer, pk=1009)

        product1 = get_object_or_404(Product, pk=3)
        product2 = get_object_or_404(Product, pk=1)

        order = Order.objects.create(customer=customer)

        # Create multiple items
        OrderItem.objects.create(
            order=order, product=product1, quantity=2, unit_price=product1.unit_price
        )

        OrderItem.objects.create(
            order=order, product=product2, quantity=20, unit_price=product2.unit_price
        )

    # Get all items for this order
    items = OrderItem.objects.filter(order=order)

    # Calculate total
    total = sum(item.quantity * item.unit_price for item in items)

    return render(
        request,
        "hello.html",
        {"customer": customer, "order": order, "items": items, "total": total},
    )
