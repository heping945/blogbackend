
import django_filters

from .models import Message,Comment



class CommentFilter(django_filters.rest_framework.FilterSet):
    exist_parent_comment = django_filters.BooleanFilter(field_name='parent_comment',lookup_expr='isnull')

    class Meta:
        model = Comment
        fields = ('post','exist_parent_comment')
