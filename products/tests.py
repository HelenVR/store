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

    def test_product_price_update(self):
        self.assertEqual(self.product.price, 699.99)
        new_price = 799.99
        self.product.price = new_price
        self.product.save()
        updated_product = Product.objects.get(id=self.product.id)
        self.assertEqual(float(updated_product.price), new_price)

    def test_product_deletion(self):
        self.assertTrue(Product.objects.filter(id=self.product.id).exists())
        self.product.delete()
        self.assertFalse(Product.objects.filter(id=self.product.id).exists())