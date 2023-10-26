from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import *
from cryptography.fernet import Fernet
import re


def navbar(request):
    return render(request, 'navbar.html')


def home(request):
    return render(request, 'home.html')


def beverages(request):
    cold_coffee = Product.objects.filter(subcategory="coldcoffee")
    cold_coffee = list(cold_coffee)
    hot_coffee = Product.objects.filter(subcategory="hotcoffee")
    hot_coffee = list(hot_coffee)
    mocktails = Product.objects.filter(subcategory="mocktails")
    mocktails = list(mocktails)
    return render(request, 'beverages.html', {'cold_coffee': cold_coffee, 'hot_coffee': hot_coffee, 'mocktails': mocktails})


def snacks(request):
    snacks = Product.objects.filter(category="snacks")
    snacks = list(snacks)
    return render(request, 'snacks.html', {'snacks': snacks})


def desserts(request):
    pudding = Product.objects.filter(subcategory="pudding")
    pudding = list(pudding)
    macaroons = Product.objects.filter(subcategory="macaroons")
    macaroons = list(macaroons)
    waffles = Product.objects.filter(subcategory="waffles")
    waffles = list(waffles)
    return render(request, 'desserts.html', {'pudding': pudding, 'macaroons': macaroons, 'waffles': waffles})


def cakes(request):
    cakes = Product.objects.filter(subcategory="cakes")
    cakes = list(cakes)
    pastries = Product.objects.filter(subcategory="pastries")
    pastries = list(pastries)
    return render(request, 'cakes.html', {'cakes': cakes, 'pastries': pastries})


def cart(request):
    if request.method == "POST":
        user = request.session.get('user')
        if user is None:
            return redirect('/login?synx=1')
        data = request.POST
        id = int(data.get('cart_id'))
        incart = data.get('incart')
        if incart == "yes":
            obj = Cart.objects.get(id=id)
            obj.quantity += 1
            obj.save()
        else:
            obj = Product.objects.get(id=id)
            try:
                cartObj = Cart.objects.get(productName=obj.productName, user=user)
                cartObj.quantity += 1
                cartObj.save()
            except:
                cartObj = Cart.objects.create(productName=obj.productName,price=obj.price,description=obj.description,image=obj.image,category=obj.category,subcategory=obj.subcategory,quantity=1,user=user)
                cartObj.save()
        return redirect(request.META.get('HTTP_REFERER'))
    user = request.session.get('user')
    if user is None:
        return redirect('/login')
    all = list(Cart.objects.filter(user=user).all())
    total = None
    if len(all) < 1:
        all = False
    else:
        total = 0
        for i in all:
            total = total + (i.price * i.quantity)
    print(all)
    return render(request, 'cart.html', {"data": all, 'total': total})


def register(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        obj = User.objects.filter(email=email)
        if obj.exists():
            return render(request, 'register.html', {'msg': "Email already exists"})

        fern = Fernet(b'nNjpIl9Ax2LRtm-p6ryCRZ8lRsL0DtuY0f9JeAe2wG0=')
        password = fern.encrypt(password.encode())
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
        fern = Fernet(b'nNjpIl9Ax2LRtm-p6ryCRZ8lRsL0DtuY0f9JeAe2wG0=')
        pas = obj[0].password
        pas = fern.decrypt(eval(pas)).decode()
        if pas != password:
            return render(request, 'login.html', {'msg': "Invalid Password"})
        else:
            request.session['user'] = obj[0].name
            return redirect('/')
    # If the request method is not POST, render the login page
    synx = request.GET.get('synx')
    if synx is not None:
        return render(request, 'login.html', {'msg': "Please login to continue"})
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

def delete_item(request):
    user = request.session.get('user')
    id = request.GET.get('id')
    path = request.GET.get('path')
    print(user, id, path)
    if user is not None and id is not None and path is not None:
        if path == "/cart/":
            obj = Cart.objects.get(id=id)
            print(obj)
            if obj.quantity <= 1:
                obj.delete()
            else:
                obj.quantity -= 1
                obj.save()
            return redirect(path)
        elif user == 'Admin':
            try:
                prodObj = Product.objects.get(id=id)
                Cart.objects.filter(productName=prodObj.productName).delete()
                prodObj.delete()
                return redirect(path)
            except:
                return redirect(path)
        else:
            return HttpResponse(status=403)
    else:
        return HttpResponse(status=404)


def serve_image(request, filename):
    return redirect('/static/imgs/' + filename)


def checkout(request):
    data = request.GET
    print(data)
    confirmed = data.get('confirmed')
    if confirmed == "yesss":
        user = request.session.get('user')
        if user is None:
            return HttpResponse(status=403)
        else:
            # Delete all the items from the cart
            c = Cart.objects.filter(user=user)
            c.delete()
            return HttpResponse(status=200)
    return render(request, 'checkout.html')
