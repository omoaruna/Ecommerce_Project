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

def single_product_view(request,id):
   product = Product.objects.get(id=id)
   context = {
       "product":product
   }
   return render(request,"products_detail.html",context)
# Create your views here.
