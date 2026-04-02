import os
import django
import random
from faker import Faker

# 1. Setup Django Environment
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "djangomosh.settings"
)  # <-- CHANGE THIS
django.setup()

# 2. Import your models
from store.models import (
    Collection,
    Product,
    Customer,
    Address,
    Order,
    OrderItem,
    Promotion,
)


def seed_db():
    fake = Faker()

    print("Clearing old data...")
    OrderItem.objects.all().delete()
    Order.objects.all().delete()
    Address.objects.all().delete()
    Customer.objects.all().delete()
    Product.objects.all().delete()
    Collection.objects.all().delete()
    Promotion.objects.all().delete()

    print("Creating Collections...")
    collection_titles = ["Electronics", "Clothing", "Home & Garden", "Sports", "Books"]
    collections = []
    for title in collection_titles:
        col = Collection.objects.create(title=title)
        collections.append(col)

    print("Creating Promotions...")
    promotions = []
    for _ in range(3):
        promo = Promotion.objects.create(
            description=fake.sentence(nb_words=4), discount=random.uniform(0.05, 0.50)
        )
        promotions.append(promo)

    print("Creating Products...")
    products = []
    for _ in range(50):
        prod = Product.objects.create(
            title=fake.catch_phrase(),
            description=fake.text(),
            slug=fake.slug(),
            unit_price=round(random.uniform(10.0, 500.0), 2),
            inventory=random.randint(0, 100),
            collection=random.choice(collections),
        )
        # Randomly assign promotions to some products
        if random.choice([True, False]):
            prod.promotions.add(random.choice(promotions))
        products.append(prod)

    print("Creating Customers and Addresses...")
    customers = []
    for _ in range(20):
        cust = Customer.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.unique.email(),
            phone=fake.phone_number()[:20],  # Truncate if faker generates long numbers
            birth_date=fake.date_of_birth(minimum_age=18, maximum_age=90),
            membership=random.choice(["B", "S", "G"]),  # Bronze, Silver, Gold
        )
        customers.append(cust)

        # Create an address for the customer
        Address.objects.create(
            street=fake.street_address(),
            city=fake.city(),
            zip_code=fake.zipcode(),
            customer=cust,
        )

    print("Creating Orders and Order Items...")
    for _ in range(30):
        order = Order.objects.create(
            customer=random.choice(customers),
            payment_status=random.choice(["P", "C", "F"]),  # Pending, Complete, Failed
        )

        # Add 1 to 5 random items to each order
        for _ in range(random.randint(1, 5)):
            OrderItem.objects.create(
                order=order,
                product=random.choice(products),
                quantity=random.randint(1, 5),
                unit_price=round(random.uniform(10.0, 500.0), 2),
            )

    print("Database seeded successfully!")


if __name__ == "__main__":
    seed_db()
