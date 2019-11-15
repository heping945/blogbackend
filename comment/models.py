import os

from django.db import models

from blog.models import Post
from accounts.models import UserProfile

# Create your models here.


class Comment(models.Model):
    content = models.CharField('内容',max_length=256,help_text='评论内容')
    parent_comment = models.ForeignKey('self', related_name='sub_comments', null=True, blank=True,verbose_name='父评论')
    reply_to = models.ForeignKey('self', related_name='who_reply', null=True, blank=True,verbose_name='回复对象')
    create_time = models.DateTimeField('创建时间', auto_now_add=True,help_text='创建时间')

    post = models.ForeignKey(Post, related_name='post_comments',verbose_name='评论的文章')
    author = models.ForeignKey(UserProfile,related_name='comment_author',verbose_name='评论人')

    def __str__(self):
        return self.author.username+'-->'+self.post.title

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['create_time']


# 定义Message文件上传路径
def message_directory_path(instance, filename):
    return os.path.join('message', instance.author.username,instance.get_message_type_display(), filename)


class Message(models.Model):
    MESSAGE_CHOICES = (
        (1, "留言"),
        (2, "bug提交"),
        (3, "反馈"),
    )
    message_type = models.PositiveIntegerField(default=1, choices=MESSAGE_CHOICES, verbose_name="留言类型",
                                      help_text="留言类型: 1(留言),2(bug提交),3(反馈)")
    subject = models.CharField("主题",max_length=100, )
    content = models.TextField("留言内容", help_text="留言内容")
    file = models.FileField(upload_to=message_directory_path, verbose_name="上传的文件", help_text="上传的文件",null=True,blank=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True,help_text='创建时间')

    author = models.ForeignKey(UserProfile,related_name='message_author',verbose_name='信息创建人')

    class Meta:
        verbose_name = "反馈消息"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.subject
