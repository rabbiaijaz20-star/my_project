from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='users_home'),
    path('login/', views.login_view, name='redirect_login'),
    path('signup/', views.signup_view, name='redirect_signup'),
]
