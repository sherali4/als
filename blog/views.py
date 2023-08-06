from django.shortcuts import render, redirect
from django.contrib.sites import requests
from django.http import HttpResponse
from .models import Company, Daraja, Profile
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

# def index(request):
#     # return HttpResponse('dasdasd asg djags jddhgasjdgh')
#     return render(request, template_name='blog/index.html')
def index(request):
    respublika = Company.objects.all().filter(turi=4, publish = 1)
    viloyat = Company.objects.all().filter(turi=7, publish = 1)
    contex = {
        'respublika':respublika,

        'viloyat': viloyat
    }
    return render(request, template_name='blog/index.html', context=contex)

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
        messages.success(request, "Tizimga xush kelibsiz")
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print('Bunday login va parol mavjud emas')

    return render(request, "users/login.html")


def register_user(request):
    form = CustomUserCreationForm()
    contex = {
        'form': form
    }
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request, "Tizimga xush kelibsiz")
            return redirect('home')
        else:
            print("Foydanaluvchi ro'yxatdan o'tmadi")
    return render(request, 'users/register.html', contex)

def logout_user(request):
    logout(request)
    messages.info(request, 'Siz tizimdan chiqdingiz')
    return redirect('login')
