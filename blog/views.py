from rest_framework import viewsets
from rest_framework.views import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from utils.permission import IsAuthorOrReadOnly
from .serializers import (CategorySerializer,TagSerializer,PostDetailSerializer,
                          PostCreateUpdateSerializer,PostSimpleSerializer)
from .models import (Category,Tag,Post,)
from .filters import PostFilter

# django-redis的缓存
from django_redis import get_redis_connection
conn = get_redis_connection("default")

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class CategoryViewset(CacheResponseMixin,viewsets.ReadOnlyModelViewSet):
    '''
    分类视图集 处理 api/category get    api/category/slug get
    '''
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    lookup_field = 'slug'
    search_fields = ('name',)

class TagViewset(viewsets.ModelViewSet):
    '''
    标签视图集 处理 api/tag get post api/tag/slug get delete put patch
    '''
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    lookup_field = 'slug'
    search_fields = ('name',)

# import redis
# r = redis.StrictRedis(host='localhost',port=6379)

class PostViewset(viewsets.ModelViewSet):
    '''
    文章视图集 处理 api/post get post api/post/id get delete put patch
    '''
    queryset = Post.objects.all()
    permission_classes = (IsAuthorOrReadOnly,IsAuthenticatedOrReadOnly)
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    # filter_fields = ('author','category','tags','create_date')
    filter_class = PostFilter
    search_fields = ('title','body')
    ordering_fields = ('create_date','views_count','mod_date')

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Post.objects.all()
        return Post.objects.filter(ifshow=True)

    # 重写retrieve方法,每次访问文章详情页redis数据incr
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        id = kwargs['pk']
        instance.views_count = conn.incr('post:{}:views'.format(id))

        # 数据库同步（即时，插眼以后改）
        views_count =int(bytes.decode(conn.get('post:{}:views'.format(id))))
        instance.views_count = views_count
        instance.save(update_fields=['views_count'])
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return PostCreateUpdateSerializer
        if self.action == 'list':
            return PostSimpleSerializer
        return PostDetailSerializer
    def perform_create(self, serializer):
        """
        重写 perform_create
        user 信息不在 request.data 中, 在保存时加入 user 信息
        """
        serializer.save(author=self.request.user)




