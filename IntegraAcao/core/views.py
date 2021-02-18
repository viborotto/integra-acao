from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required
def welcome(request):
    return render(request, "welcome.html")

@login_required
def get_home(request):
    return render(request, "home.html")

def mylogout(request):
    logout(request)
    return render(request, 'login.html')
