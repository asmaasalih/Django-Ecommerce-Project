from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.

def categories(request):
    return {'categories':Category.objects.all()}


def all_products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request,'store/all_products.html',context)

def category_list(request,category_slug):
    category = get_object_or_404(Category,slug=category_slug)
    products = Product.objects.filter(category=category)
    context = {
        'category':category,
        'products':products,
    }
    return render(request,'store/category_products.html',context)
    

def product_detail(request,slug):
    product = get_object_or_404(Product,slug=slug)
    context = {'product':product}
    return render(request,'store/product_detail.html',context)
    