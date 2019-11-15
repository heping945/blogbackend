from rest_framework import viewsets
from .serializers import UserSerializer,UserSimpleSerializer,UserRegSerializer,UserUpdateSerializer

from .models import UserProfile


class UserViewset(viewsets.ModelViewSet):
    '''
    处理api/userprofile
    '''
    queryset = UserProfile.objects.all()
    lookup_field = 'urltoken'
    ordering_fields = ('create_time',)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserSerializer
        elif self.action == 'list':
            return  UserSimpleSerializer
        elif self.action == 'create':
            return  UserRegSerializer
        return UserUpdateSerializer
