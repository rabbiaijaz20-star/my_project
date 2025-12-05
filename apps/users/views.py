from django.shortcuts import render
from django.http import HttpResponse

def home(request):
 return render(request, 'home.html')
# /users/

def login_view(request):
    return HttpResponse("Login Page")  # /users/login/

def signup_view(request):
    return HttpResponse("Signup Page")  # /users/signup/

def profile(request):
    return HttpResponse("User Profile Page")  # /users/profile/
