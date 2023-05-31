from django.contrib import admin
from django.contrib.auth.models import Group
from language.models import Language

@admin.register(Language) 
class LanguageAdmin(admin.ModelAdmin):
    pass

