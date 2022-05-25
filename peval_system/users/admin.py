from django.contrib import admin

from . models import User
from django.contrib.auth.admin import UserAdmin

# @admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        'email', 
        'first_name', 
        'last_name', 
        'is_Faculty', 
        'is_UnitHead',
        'is_DepartmentHead',
        'is_Admin',
    )
    search_fields = (
        'email',
        'first_name', 
        'last_name', 
    )
    readonly_fields = (
        'id',
        'date_joined'
    )
    filter_horizontal = ()
    list_filter = (
        'is_active',
        'date_joined'
    )
    fieldsets = ()
    ordering = ()
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_Admin', 'is_DepartmentHead', 'is_UnitHead', 'is_Faculty', 'is_superuser'),
            }
        ), 
    )

admin.site.register(User, CustomUserAdmin)

# @admin.register(FacultyProfile)
# class FacultyAdmin(admin.ModelAdmin):
#     list_display = [
#         'user', 
#         'is_assigned',
#         'is_approved',
#     ]

# @admin.register(UnitHeadProfile)
# class UnitHeadAdmin(admin.ModelAdmin):
#     list_display = [
#         'user', 
#         'is_approved',
#     ]

# @admin.register(DepartmentHeadProfile)
# class DepartmentHeadAdmin(admin.ModelAdmin):
#     list_display = [
#         'user', 
#     ]

# @admin.register(AdminProfile)
# class AdminAdmin(admin.ModelAdmin):
#     list_display = [
#         'user', 
#     ]
