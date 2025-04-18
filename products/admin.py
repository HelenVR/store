from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('name',)

    @admin.action(description='Увеличить цену на 10%')
    def increase_price(self, request, queryset):
        for product in queryset:
            product.price *= 1.10
            product.save()

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at', 'category')  # Поля, отображаемые в списке
    search_fields = ('name',)  # Поля, по которым можно искать


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Поля, отображаемые в списке