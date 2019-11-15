from django.db import models
from django.db.models import Count

from accounts.models import UserProfile
from blog.models import Post


# Create your models here.

class UserFav(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(UserProfile, verbose_name="用户")
    post = models.ForeignKey(Post, verbose_name="文章", help_text="文章id")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
        unique_together = ("user", "post")
        ordering = ['id']

    def __str__(self):
        return self.user.username

    def get_post_vote(self):
        return Post.objects.filter()


class UserVote(models.Model):
    """
    用户喜欢
    """
    VOTE_CHOICES = (
        (0, '未作选择'),
        (1, '赞同'),
        (2, '反对')
    )
    user = models.ForeignKey(UserProfile, verbose_name="用户")
    post = models.ForeignKey(Post, verbose_name="文章", help_text="文章id")
    vote = models.PositiveIntegerField(choices=VOTE_CHOICES, default=0)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    def __str__(self):
        return self.user.username + str(self.post.id)

    def __unicode__(self):
        return self.user.username + str(self.post.id)

    def get_post_upvote_count(self):
        return Post.objects.filter(uservote__post__id=self.post_id, uservote__vote=1).count()

    class Meta:
        verbose_name = '用户投票'
        verbose_name_plural = verbose_name
        unique_together = ("user", "post")
        ordering = ['id']
