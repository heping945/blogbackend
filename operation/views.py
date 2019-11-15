from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from utils.permission import IsUserOrReadOnly

from .models import UserFav, UserVote
from .serializers import UserFavSerializer, UserVoteSerializer, UserVoteUpdateSerializer


# Create your views here.

class UserFavViewset(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, IsUserOrReadOnly)
    serializer_class = UserFavSerializer
    lookup_field = 'post_id'

    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)


class UserVoteViewset(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, IsUserOrReadOnly)
    lookup_field = 'post_id'

    def get_queryset(self):
        return UserVote.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'update':
            return UserVoteUpdateSerializer
        return UserVoteSerializer


