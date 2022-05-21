from django.shortcuts import render

# Create your views here.

def signup(request):
    return render(request, 'homepage/signup.html')

def login(request):
    return render(request, 'homepage/login.html')

def checkout(request):
    return render(request, 'homepage/checkout.html')
