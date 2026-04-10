from django.contrib import admin
from . import models


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title", "product_count"]

    @admin.display()
    def product_count(self, collection):
        return collection.product_set.count()


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "unit_price",
        "inventory_status",
        "collection",
        "last_update",
    ]
    list_editable = ["unit_price"]
    list_per_page = 10
    # Adds a filter sidebar on the right
    list_filter = ("collection", "last_update")

    # Adds a search bar at the top
    search_fields = ("title", "description")

    @admin.display(ordering="inventory")
    def inventory_status(self, product):
        if product.inventory < 10:
            return "Low"
        return "OK"


admin.site.register(models.Promotion)


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "phone", "membership"]
    list_editable = ["membership"]
    list_per_page = 10


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "customer", "placed_at", "payment_status"]
    list_per_page = 10
    list_select_related = ["customer"]
    list_filter = ["payment_status"]
    search_fields = [
        "customer__first_name__istartswith",
        "customer__last_name__istartswith",
    ]
    list_display_links = ["customer"]
