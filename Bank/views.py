from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, 'Home.html')


def login(request, username=None, password=None):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('new')
        else:
            messages.info(request, "invalid login")
            return redirect('logout')
    return render(request, "Login.html")



def register(request):
    if request.method == 'POST':
        username = request.POST['username']

        password = request.POST['password']
        cnfpassword = request.POST['cnfpassword']
        if password == cnfpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already taken")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                return redirect('login')


        else:
            messages.info(request, 'password not match')
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")



def logout(request):
    auth.logout(request)
    return redirect('/')


def new(request):
    return render(request, 'New.html')


def form(request):
    return render(request, 'Form.html')


def accept(request):
    return render(request, 'Accept.html')
