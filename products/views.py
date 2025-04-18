from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm
from django.shortcuts import render, redirect, get_object_or_404


def home_view(request):
    return render(request, 'products/home.html')


def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})


def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'products/product_form.html', {'form': form})


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')