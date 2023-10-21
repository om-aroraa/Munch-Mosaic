from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request, 'cakes.html')

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
    return render(request, 'adminmenu.html')
