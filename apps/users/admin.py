from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomerUser, UserProfile, Subscription

class CustomerUserAdmin(UserAdmin):
    model = CustomerUser
    list_display = ('username', 'email', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('profile_picture', 'bio')}),
    )

admin.site.register(CustomerUser, CustomerUserAdmin)
admin.site.register(UserProfile)
admin.site.register(Subscription)
