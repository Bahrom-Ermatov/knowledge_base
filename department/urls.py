from django.urls import path, include
from rest_framework import routers

from department.views import DepartmentViewSet

router = routers.DefaultRouter()
router.register("departments", DepartmentViewSet, "departments")

urlpatterns = [
    path('', include(router.urls)),
]
