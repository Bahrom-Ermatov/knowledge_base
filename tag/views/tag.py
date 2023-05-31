from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.decorators import action

from tag.models import Tag
from tag.serializers import TagSerializer

class TagViewSet(GenericViewSet, 
                  mixins.ListModelMixin,  mixins.RetrieveModelMixin, 
                  mixins.UpdateModelMixin, mixins.CreateModelMixin): 

    permission_classes = [AllowAny]
    queryset = Tag.objects.all()
    serializer_class = Tag



