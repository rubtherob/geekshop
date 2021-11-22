import json

from django.core.management import BaseCommand

from mainapp.models import ProductCategory, Product

JSON_PATH = 'mainapp/fixtures'

def load_from_json(file_name):
    with open(file_name, mode='r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('Category.json')

        ProductCategory.objects.all().delete()
        for category in categories:
            cat = category.get('fields')
            cat['id'] = category.get('pk')
            new_category = ProductCategory(**cat)
            new_category.save()

        products = load_from_json('products.json')

        Product.objects.all().delete()
        for product in products:
            prod = product.get('fields')
            category = prod.get('category')
            _category = Product.objects.get(id=category)
            prod['category'] = _category
            new_category = Product(**prod)
            new_category.save()