from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import *
from django.contrib import messages
import re


def navbar(request):
    return render(request, 'navbar.html')


def checkout(request):
    return render(request, 'checkout.html')


def home(request):
    return render(request, 'home.html')


def beverages(request):
    return render(request, 'beverages.html')


def snacks(request):
    return render(request, 'snacks.html')


def desserts(request):
    return render(request, 'desserts.html')


def cakes(request):
    cakes = Product.objects.filter(category="cakes")
    cakes = list(cakes)
    pastries = Product.objects.filter(category="pastries")
    pastries = list(pastries)
    return render(request, 'cakes.html', {'cakes': cakes})


def cart(request):
    return render(request, 'cart.html')


def register(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        obj = User.objects.filter(email=email)
        if obj.exists():
            return render(request, 'register.html', {'msg': "Email already exists"})
        
        obj = User.objects.create(name=name, email=email, password=password)
        obj.save()
        request.session['user'] = name
        return redirect('/')
    else:
        # check if session has msg
        if request.session.get('msg'):
            msg = request.session['msg']
            del request.session['msg']
            return render(request, 'register.html', {'msg': msg})
        else:
            return render(request, 'register.html')


def login(request):
    # Check if the request method is POST
    if request.method == "POST":
        # Get the POST data from the request
        data = request.POST
        # Extract the email and password from the POST data
        email = data.get('email')
        password = data.get('password')
        # Check if the email is valid using a regular expression
        email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        if not re.search(email_regex, email):
            # If the email is not valid, render the login page with an error message
            return render(request, 'login.html', {'msg': "Invalid Credentials"})
        # Check if a user with the given email exists in the database
        obj = User.objects.filter(email=email)
        if len(obj) == 0:
            # If the email does not exist, render the login page with an error message
            return render(request, 'login.html', {'msg': "Email does not exist"})
        # Check if a user with the given email and password exists in the database
        obj = User.objects.filter(email=email, password=password)
        if len(obj) == 1:
            # If the email and password are valid, redirect to the home page
            user = User.objects.get(email=email)
            request.session['user'] = user.name
            return redirect('/')
        else:
            # If the password is invalid, render the login page with an error message
            return render(request, 'login.html', {'msg': "Invalid Password"})
    # If the request method is not POST, render the login page
    return render(request, 'login.html')

def logout(request):
    del request.session['user']
    return redirect('/')



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
    queryset = Product.objects.get(id=id)
    queryset.delete()
    return redirect('/adminmenu')
