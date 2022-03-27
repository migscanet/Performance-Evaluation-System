from django.contrib import admin

from . models import User, FacultyProfile, UnitHeadProfile, DepartmentHeadProfile, AdminProfile

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'up_email', 
        'first_name', 
        'last_name', 
        'is_Faculty', 
        'is_UnitHead',
        'is_DepartmentHead',
        'is_Admin',
    ]

@admin.register(FacultyProfile)
class FacultyAdmin(admin.ModelAdmin):
    list_display = [
        'user', 
        'is_assigned',
        'is_approved',
    ]

@admin.register(UnitHeadProfile)
class UnitHeadAdmin(admin.ModelAdmin):
    list_display = [
        'user', 
        'is_approved',
    ]

@admin.register(DepartmentHeadProfile)
class DepartmentHeadAdmin(admin.ModelAdmin):
    list_display = [
        'user', 
    ]

@admin.register(AdminProfile)
class AdminAdmin(admin.ModelAdmin):
    list_display = [
        'user', 
    ]
