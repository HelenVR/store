from django.contrib import admin
from django.urls import path, include
from products.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Добавляем маршрут для корня сайта
    path('products/', include('products.urls')),  # Подключаем URLs приложения products
]