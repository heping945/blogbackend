from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import UserProfile


class CustomBackend(ModelBackend):
    """邮箱也能登录"""
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user=UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None