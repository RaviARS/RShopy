from django.shortcuts import render, redirect


def home(request):
    return render(request, 'shop/home.html')


def shop(request):
    return render(request, 'shop/shop.html')


def cart(request):
    return render(request, 'shop/cart.html')


def product_details(request):
    return render(request, 'shop/product_details.html')


def checkout(request):
    return render(request, 'shop/checkout.html')

