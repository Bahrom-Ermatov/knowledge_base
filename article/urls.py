from django.urls import path, include
from rest_framework import routers

from article.views import ArticleViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register("articles", ArticleViewSet, "articles")
router.register("comments", CommentViewSet, "comments")

urlpatterns = [
    path('', include(router.urls)),
]
