from django.db import models

from tasks import notify_product_change


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk is not None:
            action = 'updated'
        else:
            action = 'added'
        super().save(*args, **kwargs)
        notify_product_change.delay(self.name, action)

    def delete(self, *args, **kwargs):
        product_name = self.name
        super().delete(*args, **kwargs)
        notify_product_change.delay(product_name, 'removed')
