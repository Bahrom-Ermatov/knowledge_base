from django.urls import path, include
from rest_framework import routers

from language.views import LanguageViewSet

router = routers.DefaultRouter()
router.register("languages", LanguageViewSet, "languages")

urlpatterns = [
    path('', include(router.urls)),
]
