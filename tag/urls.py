from django.urls import path, include
from rest_framework import routers

from tag.views import TagViewSet

router = routers.DefaultRouter()
router.register("tags", TagViewSet, "tags")

urlpatterns = [
    path('', include(router.urls)),
]
