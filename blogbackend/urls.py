"""blogbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import xadmin
from rest_framework.documentation import include_docs_urls

from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse('index.html')


urlpatterns = [
    # url(r'^$', index),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),

    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api/(?P<version>(v1|v2))/', include('api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/docs/', include_docs_urls(title='hpapi')),
    url('', include('social_django.urls', namespace='social'))  # 第三方登录
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
