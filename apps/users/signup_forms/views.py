from django.shortcuts import render

def home(request):
    return render(request, 'signup_forms/home.html')

def login_view(request):
    return render(request, 'signup_forms/login.html')

def signup_view(request):
    return render(request, 'signup_forms/signup.html')
