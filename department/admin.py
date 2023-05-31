from django.contrib import admin
from django.contrib.auth.models import Group
from department.models import Department

@admin.register(Department) 
class DepartmentAdmin(admin.ModelAdmin):
    pass

