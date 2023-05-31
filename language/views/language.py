from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.decorators import action

from language.models import Language
from language.serializers import LanguageSerializer

class LanguageViewSet(GenericViewSet, 
                  mixins.ListModelMixin,  mixins.RetrieveModelMixin, 
                  mixins.UpdateModelMixin, mixins.CreateModelMixin): 

    permission_classes = [AllowAny]
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

