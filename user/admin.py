from django.contrib import admin
from django.contrib.auth.models import Group
from user.models import User, Role_group, User_role

@admin.register(Role_group) 
class RoleGroupAdmin(admin.ModelAdmin):
    pass

@admin.register(User_role) 
class UserRoleAdmin(admin.ModelAdmin):
    pass

@admin.register(User) 
class UserAdmin(admin.ModelAdmin):
    pass

