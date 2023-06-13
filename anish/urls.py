from django.contrib import admin
from django.urls import path
from anish import views

urlpatterns = [
    path("",views.index, name="home"),
    path("about", views.about, name="about"),
    path("eggroll", views.eggroll, name="eggroll"),
    path("contact", views.contact, name="contact"),
    path("chicken", views.chicken, name="chicken"),
    path("motton", views.motton, name="motton"),
    path("mixed", views.mixed, name="mixed"),
    path("register", views.register, name="register"),
    path("cart", views.cart, name="cart"),
    path("login", views.Login, name="login")



]