from django.shortcuts import render
from .models import Product

product = Product.objects.all()
context = {
    "all_products" : product
} 

def product_page(request):

    return render(request,"product.html",context)

def about(request):
    return render(request,"about.html")
# Create your views here.
