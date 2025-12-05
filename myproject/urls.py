from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.signup_forms.urls')),  # signup/login URLs
    path('profile/', include('apps.users.user_profile.urls')),  # profile URLs
]
