from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
    # Add additional fields to display in the user list view
    list_display = ('email', 'first_name', 'last_name', 'phone_number', 'gender', 'date_of_birth', 'is_staff')
    
    # Add new sections in fieldsets to include additional user fields
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', 'gender', 'date_of_birth', 'image')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    # Optionally, add the fields to add_fieldsets for user creation form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'phone_number', 'gender', 'date_of_birth', 'image', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser'),
        }),
    )
