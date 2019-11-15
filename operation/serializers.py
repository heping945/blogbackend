from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import UserFav, UserVote
from blog.models import Post


class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'post'),
                message="已经收藏"
            )
        ]

        fields = ("user", "post", "id")


class UserVoteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    post_title = serializers.CharField(source='post.title', read_only=True)
    get_post_upvote_count = serializers.CharField(read_only=True)

    class Meta:
        model = UserVote
        validators = [
            UniqueTogetherValidator(
                queryset=UserVote.objects.all(),
                fields=('user', 'post'),
                message="已经投票"
            )
        ]

        fields = ("user", "post", "id", 'vote', 'post_title', 'get_post_upvote_count')

    def create(self, validated_data):
        vote = validated_data['vote']
        post = validated_data['post']
        post_obejct = Post.objects.filter(id=post.id).first()
        if vote == 2:
            post_obejct.upvote_count -= 1
        else:
            post_obejct.upvote_count += 1
        post_obejct.save(update_fields=['upvote_count'])

        return super().create(validated_data)


class UserVoteUpdateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    post_title = serializers.CharField(source='post.title', read_only=True)

    class Meta:
        model = UserVote
        fields = ("user", "id", 'vote', 'post_title')

    def update(self, instance, validated_data):
        instance_vote = instance.vote               # uservote实例
        update_vote = validated_data['vote']        # 前端传来的vote参数，选项有0，1，2(无，+1，-1)
        post_id = instance.post_id                  # 对应的post实例
        # print(instance_vote)
        # print(update_vote)
        post = Post.objects.filter(id=post_id).first()
        # print(post)
        if instance.vote ==0:
            if update_vote ==1:
                post.upvote_count+=1
            else:
                post.upvote_count -=1
        elif instance.vote ==2:
            post.upvote_count += 1
        else:
            if update_vote ==2:
                post.upvote_count -= 2
            else:
                post.upvote_count -= 1
        post.save(update_fields=['upvote_count'])
        return super().update(instance, validated_data)

