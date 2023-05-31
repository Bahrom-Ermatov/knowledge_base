from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.decorators import action

from user.models import User_role
from user.serializers import UserRoleSerializer

class UserRoleViewSet(GenericViewSet, 
                  mixins.ListModelMixin,  mixins.RetrieveModelMixin, 
                  mixins.UpdateModelMixin, mixins.CreateModelMixin): 

    permission_classes = [AllowAny]
    queryset = User_role.objects.all()
    serializer_class = UserRoleSerializer


