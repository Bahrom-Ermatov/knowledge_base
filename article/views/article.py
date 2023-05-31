from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.decorators import action

from article.models import Article
from article.serializers import ArticleSerializer

class ArticleViewSet(GenericViewSet, 
                  mixins.ListModelMixin,  mixins.RetrieveModelMixin, 
                  mixins.UpdateModelMixin, mixins.CreateModelMixin): 

    permission_classes = [AllowAny]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


