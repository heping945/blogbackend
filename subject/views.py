from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from rest_framework import viewsets, mixins

from .models import Topic, Chapter
from .serializers import ChapterSerializer, ChapterSimpleSerializer, TopicSerializer, ChapterDetailSerializer


class TopicViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,viewsets.GenericViewSet):
    '''
    标签视图集 处理 api/tag get post api/tag/slug get delete put patch
    '''
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    lookup_field = 'urltag'
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        if self.request.user.username == 'heping':
            return Topic.objects.all()
        return Topic.objects.filter(ifshow=True)

class ChapterFileViewset(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    filter_fields = ('topic__urltag','topic','topic__ifshow')

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Chapter.objects.all()
        return Chapter.objects.filter(topic__ifshow=True)

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy', 'partial_update']:
            return (IsAdminUser(),)
        return []


    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return ChapterSerializer
        elif self.action == 'list':
            return ChapterSimpleSerializer
        return ChapterDetailSerializer
