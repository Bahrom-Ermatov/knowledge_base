from django.contrib import admin
from django.contrib.auth.models import Group
from article.models import Article, Comment

admin.site.unregister(Group)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment) 
class CommentAdmin(admin.ModelAdmin):
    pass

