from django.contrib import admin, messages
from django.urls import reverse
from django.utils.html import format_html
from urllib.parse import urlencode
from . import models


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title", "product_count"]
    search_fields = ["title"]

    @admin.display()
    def product_count(self, collection):
        return collection.product_set.count()


class InventoryFilter(admin.SimpleListFilter):
    title = "inventory"
    parameter_name = "inventory_status"

    def lookups(self, request, model_admin):
        return [
            ("Low", "Low"),
            ("OK", "OK"),
            ("Empty", "Empty"),
        ]

    def queryset(self, request, queryset):

        if self.value() == "Low":
            return queryset.filter(inventory__lt=10, inventory__gt=0)
        if self.value() == "OK":
            return queryset.filter(inventory__gte=10)
        if self.value() == "Empty":
            return queryset.filter(inventory=0)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ["collection"]
    prepopulated_fields = {"slug": ["title"]}
    actions = ["clear_inventory"]
    list_display = [
        "title",
        "unit_price",
        "inventory",
        "inventory_status",
        "collection",
        "last_update",
    ]
    list_editable = ["unit_price", "inventory"]
    list_per_page = 10
    # Adds a filter sidebar on the right
    list_filter = ("collection", "last_update", InventoryFilter)

    # Adds a search bar at the top
    search_fields = ("title", "description")

    @admin.display(ordering="inventory")
    def inventory_status(self, product):
        if product.inventory == 0:
            return "Empty"
        elif product.inventory < 10:
            return "Low"
        return "OK"

    @admin.action(description="Clear inventory")
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f"{updated_count} products inventory cleared.",
            messages.ERROR,
        )


admin.site.register(models.Promotion)


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "phone", "membership", "orders"]
    list_editable = ["membership"]
    list_per_page = 10
    search_fields = ["first_name__istartswith", "last_name__istartswith"]
    ordering = ["first_name", "last_name"]

    @admin.display(ordering="orders__count")
    def orders(self, customer):
        url = (
            reverse("admin:store_order_changelist")
            + "?"
            + urlencode({"customer__id": str(customer.id)})
        )
        return format_html("<a href='{}'>{}</a>", url, customer.order_set.count())


class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
    autocomplete_fields = ["product"]
    extra = 0


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    autocomplete_fields = ["customer"]
    list_display = ["id", "customer", "placed_at", "payment_status"]
    list_per_page = 10
    list_select_related = ["customer"]
    list_filter = ["payment_status"]
    search_fields = [
        "customer__first_name__istartswith",
        "customer__last_name__istartswith",
    ]
    list_display_links = ["customer"]
