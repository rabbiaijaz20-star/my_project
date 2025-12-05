from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomerUser, SignupForm

@admin.register(CustomerUser)
class CustomerUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number',)}),
    )

@admin.register(SignupForm)
class SignupFormAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'email', 'created_at')
