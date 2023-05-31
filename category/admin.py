from django.contrib import admin
from django.contrib.auth.models import Group
from category.models import Category

@admin.register(Category) 
class CategoryAdmin(admin.ModelAdmin):
    pass

