from django.urls import path
from .views import product_create_view, home_view, product_list_view, product_detail_view


urlpatterns = [
    path('', home_view, name='home'),
    path('products/', product_list_view, name='product_list'),
    path('products/new/', product_create_view, name='product_create'),
    path('products/<int:pk>/', product_detail_view, name='product_detail'),
]