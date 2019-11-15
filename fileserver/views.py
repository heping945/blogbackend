from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import PostImg
from .serializers import PostImgSerializer



class PostImgViewset(mixins.RetrieveModelMixin,mixins.ListModelMixin,
                  mixins.CreateModelMixin,viewsets.GenericViewSet):
    queryset = PostImg.objects.all()
    serializer_class = PostImgSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    ordering_fields = ('created_time',)