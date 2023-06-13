from django.shortcuts import render, HttpResponse
from datetime import datetime
from anish.models import Contact, Register
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

print(make_password('1234'))

def index(request):
    context = {
        "varibles": "That is sent",
    }
    # return HttpResponse("This is home page")
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def cart(request):
    if request.method == 'POST':
        messages.success(request, 'This message has been sent.')
    return render(request, "cart.html")


def eggroll(request):
    return render(request, "eggroll.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'This message has been sent.')
    return render(request, "contact.html")


def chicken(request):
    return render(request, "chicken.html")


def motton(request):
    return render(request, "motton.html")


def mixed(request):
    return render(request, "mixed.html")


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pwd')
        pass2 = request.POST.get('pwd2')
        print(name, email, pass1, pass2)
        register = Register(name=name, email=email, pass1=pass1, pass2=pass2)
        register.save()
        if pass2 != pass1:
            messages.error(request, "Password donot match")
        else:
            messages.success(request, 'Register sucessfully.')

    return render(request, "register.html")


def Login(request):
    if request.method == 'POST':
        loginemail = request.POST.get('email')
        loginpass = request.POST.get('pwd')
        user = authenticate(email=loginemail,passowrd=loginpass)
        if  user is not None:
            Login(request,user)
            messages.success(request,"Succefully logged in")
            return render(request,"base.html")
        else:
            messages.error(request,"Invalid Credential")
    return render(request, "login.html")
           

    

# Create your views here.
