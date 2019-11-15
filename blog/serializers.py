from rest_framework import serializers
from django.contrib.auth import get_user_model

from  .models import Category,Tag,Post
from  accounts.serializers import UserSimpleSerializer

User = get_user_model()


class ParentsSerialziser(serializers.ModelSerializer):
    '''
    父分类序列
    '''
    slug = serializers.CharField(help_text="slug", label="slug",read_only=True)
    class Meta:
        model = Category
        fields = '__all__'

class CategorySubSerializer(serializers.HyperlinkedModelSerializer):
    slug = serializers.CharField(help_text="slug", label="slug",read_only=True)
    parent_category = ParentsSerialziser()
    get_post_count = serializers.CharField(read_only=True)
    class Meta:
        model = Category
        fields = ('url','id','name','slug','parent_category','get_post_count')
        extra_kwargs = {
            'url': {'view_name': 'category-detail', 'lookup_field': 'slug'},
        }

class SimplePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','title')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    slug = serializers.CharField(help_text="slug", label="slug",read_only=True)
    parent_category = ParentsSerialziser()
    get_post_count = serializers.CharField(read_only=True)
    sub_cat = CategorySubSerializer(many=True)
    # cat_post = serializers.CharField(source='cat_post.id')
    cat_post = SimplePostSerializer(many=True)
    class Meta:
        model = Category
        fields = ('url','id','name','slug','parent_category','get_post_count','sub_cat','cat_post')
        extra_kwargs = {
            'url': {'view_name': 'category-detail', 'lookup_field': 'slug'},
        }


class TagSerializer(serializers.HyperlinkedModelSerializer):
    slug = serializers.CharField(help_text="slug", label="slug",read_only=True)
    get_post_count = serializers.CharField(read_only=True)
    class Meta:
        model = Tag
        fields = ('url','id','slug','name','get_post_count')
        extra_kwargs = {
            'url': {'view_name': 'tag-detail','lookup_field':'slug'},
        }
    def validate_name(self,name):
        if len(name) == 1:
            raise serializers.ValidationError('太短了')
        return name

class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
    # category = serializers.CharField(source='category.get_absolute_url')
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    author = UserSimpleSerializer()
    create_date = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    class Meta:
        model = Post
        fields = ('url', 'id','title', 'body','body_md', 'can_comment','excerpt','codestyle',
                  'views_count', 'comment_count', 'upvote_count','create_date','mod_date',
                  'reproduce_source','reproduce','author','category', 'tags','get_post_comment_count')


class PostCreateUpdateSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(),many=True)
    class Meta:
        model = Post
        fields = ('url','id','title','body','body_md','reproduce','codestyle','reproduce_source','can_comment','category','tags')

class PostSimpleAuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields =('username','nickname','avatar')


# list序列化
class PostSimpleSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.CharField(source="category.name")
    category_slug = serializers.CharField(source='category.slug')
    category_url = serializers.CharField(source='category.get_absolute_url')
    author = PostSimpleAuthorSerializer()
    create_date = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    mod_date = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = Post
        fields = ('url','id','title','excerpt','create_date','mod_date','views_count','comment_count','upvote_count',
                  'author','category','category_slug','category_url','get_post_comment_count')


