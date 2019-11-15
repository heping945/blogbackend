from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Comment, Message
from blog.models import Post

User = get_user_model()


# 评论 用户 （用户名，头像）
class CommentUserSerialziser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'avatar')



# 评论 文章 （id 标题）
class CommentPostSerialziser(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title')



# 评论的回复评论
class ReplyCommentSerializer(serializers.ModelSerializer):
    author = CommentUserSerialziser()
    class Meta:
        model = Comment
        fields = ['id', 'author',]


# 评论的父评论 （id 内容 作者）
class CommentParSerialziser(serializers.ModelSerializer):
    author = CommentUserSerialziser()
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    class Meta:
        model = Comment
        fields = ('id', 'content', 'author','create_time')


# 评论的子评论 （id 内容 作者 回复对象）
class CommentSubSerialziser(serializers.ModelSerializer):
    author = CommentUserSerialziser()
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    reply_to = ReplyCommentSerializer()
    parent_comment = serializers.CharField(source='parent_comment_id')
    class Meta:
        model = Comment
        fields = ('id', 'content', 'author', 'reply_to','create_time','parent_comment')


# （id，内容，文章，作者，创建事件，子评论，父评论）----->(对应的是 get_object)
class CommentSerialziser(serializers.ModelSerializer):
    post = CommentPostSerialziser()
    author = CommentUserSerialziser()
    sub_comments = CommentSubSerialziser(many=True)
    parent_comment = CommentParSerialziser()
    reply_to = ReplyCommentSerializer()
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    class Meta:
        model = Comment
        fields = ('id', 'content', 'post', 'author', 'create_time', 'sub_comments', 'parent_comment','reply_to')


class CommentCreateSerializer(serializers.ModelSerializer):
    author = CommentUserSerialziser(read_only=True)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    sub_comments = CommentSubSerialziser(many=True,read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'content', 'post', 'reply_to', 'parent_comment','author','create_time','sub_comments')


# 以下是反馈消息序列化

class MessageSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = Message
        fields = ('id', "author", "message_type", "subject", "content", "file", "create_time")
