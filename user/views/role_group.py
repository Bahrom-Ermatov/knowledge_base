from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.decorators import action

from user.models import Role_group
from user.serializers import RoleGroupSerializer

class RoleGroupViewSet(GenericViewSet, 
                  mixins.ListModelMixin,  mixins.RetrieveModelMixin, 
                  mixins.UpdateModelMixin, mixins.CreateModelMixin): 

    permission_classes = [AllowAny]
    queryset = Role_group.objects.all()
    serializer_class = RoleGroupSerializer




