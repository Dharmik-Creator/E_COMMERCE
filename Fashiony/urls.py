from django.contrib import admin
from django.urls import path
from Fashiony import views

urlpatterns = [
    path("", views.Index , name="Index"),
    path("products", views.Products , name="Products"),
    path("product_details", views.Product_Details , name="Product_Details"),
    path("cart", views.Cart , name="Cart"),
    path("account", views.Account , name="Account"),
    
]
