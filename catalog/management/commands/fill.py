import random

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = []
        for i in range(5):
            category_list.append(
                Category(
                    name=f"Category#{i + 1}",
                    description=f"this is another catecory #{i + 1}"
                )
            )

        Category.objects.bulk_create(category_list)

        category_id_list = list(Category.objects.all().values_list('id', flat=True))
        max_id = max(category_id_list)
        min_id = min(category_id_list)

        product_list = []
        for i in range(50):
            product_list.append(
                Product(
                    name=f"Product#{i}",
                    description=f"this is description for product #{i}",
                    category_id=random.randint(max_id, min_id),
                    price=random.random() * 1000
                )
            )

        Product.objects.bulk_create(product_list)


# from django.core.management import BaseCommand
# import json
# from catalog.models import Category, Product
# from django.db import connection
#
# class Command(BaseCommand):
#
#     def handle(self, *args, **kwargs):
#         with connection.cursor() as cursor:
#             cursor.execute(f'TRUNCATE TABLE catalog_category RESTART IDENTITY CASCADE;')
#
#
#         Category.objects.all().delete()
#         Product.objects.all().delete()
#
#         with open('data.json', encoding='utf-8') as json_file:
#             data = json.load(json_file)
#
#             product_for_create = []
#             category_for_create = []
#
#             for category in data:
#                 if category["model"] == "catalog.category":
#                     category_for_create.append(Category(category_name=category["fields"]['category_name'],
#                                                         category_description=category["fields"]['category_description']))
#             Category.objects.bulk_create(category_for_create)
#             for product in data:
#                 if product["model"] == "catalog.product":
#                     product_for_create.append(Product(product_name=product["fields"]['product_name'],
#                                                       description=product["fields"]['description'],
#                                                       category=Category.objects.get(pk=product["fields"]['category']),
#                                                       price=product["fields"]['price']))
#
#             Product.objects.bulk_create(product_for_create)
