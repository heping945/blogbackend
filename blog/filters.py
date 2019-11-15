import django_filters
from django.db.models import Q

from .models import Post, Tag, Category


class PostFilter(django_filters.rest_framework.FilterSet):
    '''
    标签的过滤类
    '''
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    body = django_filters.CharFilter(field_name='body', lookup_expr='icontains')
    min_id = django_filters.NumberFilter(field_name='id', lookup_expr='gt')
    max_id = django_filters.NumberFilter(field_name='id', lookup_expr='lt')
    top_category = django_filters.NumberFilter(method='top_category_filter',label='分类高级' )

    # 理解，分类的父分类也包括子分类的文章，即文章的分类的父分类也包括此文章
    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value) | Q(
            category__parent_category__parent_category__parent_category_id=value))

    class Meta:
        model = Post
        fields = ['title', 'body', 'min_id', 'max_id', 'author__username', 'category', 'tags', 'top_category']
