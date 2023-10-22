from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import *


def navbar(request):
    return render(request, 'navbar.html')


def home(request):
    return render(request, 'home.html')


def beverages(request):
    return render(request, 'beverages.html')


def snacks(request):
    return render(request, 'snacks.html')


def desserts(request):
    return render(request, 'desserts.html')


def cakes(request):
    cakes = Product.objects.filter(subcategory="waffles")
    cakes = list(cakes)
    return render(request, 'cakes.html', {'cakes': cakes})


def cart(request):
    return render(request, 'cart.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def checkout(request):
    return render(request, 'checkout.html')


def footer(request):
    return render(request, 'footer.html')


def cursor(request):
    return render(request, 'cursor.html')


def adminmenu(request):
    if request.method == "POST":
        data = request.POST
        productName = data.get('productName')
        price = data.get('price')
        description = data.get('description')
        image = request.FILES.get('image')
        category = data.get('category')
        subcategory = data.get('subcategory')

        Product.objects.create(productName=productName,
                               price=price,
                               description=description,
                               image=image,
                               category=category,
                               subcategory=subcategory
                               )

        return redirect('/adminmenu')
    else:
        return render(request, 'adminmenu.html')


def delete_menu(request, id):
    queryset = Product.objects.get(id = id)
    queryset.delete()
    return redirect('/adminmenu')
