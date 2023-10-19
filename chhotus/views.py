from django.http import HttpResponse
from django.shortcuts import render

def navbar(request):
    return render(request, 'navbar.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def beverages(request):
    return render(request, 'beverages.html')

def snacks(request):
    return render(request, 'snacks.html')

def desserts(request):
    return render(request, 'desserts.html')

def cart(request):
    return render(request, 'cart.html')

def meals(request):
    return render(request, 'meals.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def checkout(request):
    return render(request, 'checkout.html')

def footer(request):
    return render(request, 'footer.html')
