from rest_framework import viewsets
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .models import Info
from .serializers import InfoSerializer

class InfoViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
