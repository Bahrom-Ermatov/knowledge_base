from django.contrib import admin
from django.contrib.auth.models import Group
from tag.models import Tag

@admin.register(Tag) 
class TagAdmin(admin.ModelAdmin):
    pass


