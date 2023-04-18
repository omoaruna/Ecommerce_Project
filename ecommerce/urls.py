from django.urls import path
from .views import *

urlpatterns = [
    path("",product_page, name = "product_page"),
    path("about/",about, name="about")
]
