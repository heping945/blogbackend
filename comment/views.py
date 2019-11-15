from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticatedOrReadOnly

from utils.permission import IsAuthorOrReadOnly
from .models import Comment,Message
from .filters import CommentFilter
from .serializers import CommentSerialziser,CommentCreateSerializer,MessageSerializer


# Create your views here.


class CommentViewSet(mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.ListModelMixin, mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    permission_classes = (IsAuthorOrReadOnly,IsAuthenticatedOrReadOnly)
    filter_class = CommentFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return CommentCreateSerializer
        return CommentSerialziser

    def perform_create(self, serializer):
        """
        重写 perform_create
        user 信息不在 request.data 中, 在保存时加入 user 信息
        """
        serializer.save(author=self.request.user)


class MessageViewset(mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin,
                            viewsets.GenericViewSet):

    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)
    filter_fields = ('message_type',)

    serializer_class = MessageSerializer
    queryset = Message.objects.all()
