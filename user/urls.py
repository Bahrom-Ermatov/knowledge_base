from django.urls import path, include
from rest_framework import routers

from user.views import UserViewSet, RoleGroupViewSet, UserRoleViewSet

router = routers.DefaultRouter()
router.register("users", UserViewSet, "users")
router.register("role_groups", RoleGroupViewSet, "role_groups")
router.register("user_roles", UserRoleViewSet, "user_roles")

urlpatterns = [
    path('', include(router.urls)),
]
