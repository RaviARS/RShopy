from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('shop', views.shop, name='shop'),
    path('cart', views.cart, name='cart'),
    path('product-details', views.product_details, name='product-details'),
    path('checkout', views.checkout, name='checkout'),
]
