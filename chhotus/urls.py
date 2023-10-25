"""
URL configuration for chhotus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name='home'),
    path("navbar/", navbar, name="navbar"),
    path("beverages/", beverages, name="beverages"),
    path("snacks/", snacks, name="snacks"),
    path("desserts/", desserts, name="desserts"),
    path("cakes/", cakes, name="cakes"),
    path("cart/", cart, name="cart"),
    path("checkout/", checkout, name="checkout"),
    path("login/", login, name="login"),
    path("register/", register, name="register"),   
    path("cursor/", cursor, name="cursor"),
    path("adminmenu/", adminmenu, name="adminmenu"),
    path('logout/', logout, name="logout"),
    path('del', delete_item, name='delete'),
    path('home/static/imgs/<str:filename>', serve_image, name="serve_image"),
]
