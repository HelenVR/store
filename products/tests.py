from django.test import TestCase
from .models import Category, Product


class CategoryModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Electronics', description='Devices and gadgets')

    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Electronics')
        self.assertEqual(self.category.description, 'Devices and gadgets')


class ProductModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Electronics', description='Devices and gadgets')
        self.product = Product.objects.create(name='Smartphone', description='Latest model smartphone', price=699.99, category=self.category)

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Smartphone')
        self.assertEqual(self.product.description, 'Latest model smartphone')
        self.assertEqual(self.product.price, 699.99)
        self.assertEqual(self.product.category.name, 'Electronics')