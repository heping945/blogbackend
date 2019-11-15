# api接口的urls文件
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token

from django.conf.urls import url, include

from blog.views import (PostViewset, TagViewset, CategoryViewset)
from accounts.views import UserViewset
from fileserver.views import PostImgViewset
from subject.views import TopicViewset,ChapterFileViewset
from operation.views import UserFavViewset,UserVoteViewset
from comment.views import CommentViewSet,MessageViewset
from info.views import InfoViewset

router = DefaultRouter()

router.register(r'users', UserViewset, base_name='user')
router.register(r'categories', CategoryViewset, base_name='category')
router.register(r'tags', TagViewset, base_name='tag')
router.register(r'posts', PostViewset, base_name='post')
router.register(r'topics', TopicViewset, base_name='topic')
router.register(r'postimg', PostImgViewset)
router.register(r'userfavs', UserFavViewset,base_name="userfavs")
router.register(r'uservote', UserVoteViewset,base_name="uservote")
router.register(r'comments', CommentViewSet,base_name="comments")
router.register(r'messages', MessageViewset,base_name="messages")
router.register(r'chapters', ChapterFileViewset)
router.register(r'info', InfoViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
    # 登录接口
    url(r'^login/$', obtain_jwt_token),
    # jwt token刷新延长登录接口
    url(r'^refresh/$', refresh_jwt_token),
]
