import os

from django.db import models


# Create your models here.


class Topic(models.Model):
    title = models.CharField('标题', help_text='标题', max_length=64, unique=True)
    urltag = models.CharField('标签', help_text='标签', max_length=32, unique=True,null=False,blank=False)
    reproduce = models.BooleanField('是否转载', default=False, help_text='是否转载')
    reproduce_source = models.URLField('转载来源地址', max_length=512, null=True, blank=True, help_text='转载来源地址')
    create_date = models.DateTimeField('创建时间', auto_now_add=True, help_text='创建时间')
    codestyle = models.CharField('代码风格', max_length=24, help_text='代码风格', blank=True, null=True, default='monokai')
    desc = models.TextField(default="", max_length=200, verbose_name="主题描述", help_text="主题描述")
    img = models.ImageField('图片', upload_to='subject/topic/', null=True, blank=True)
    ifshow = models.BooleanField('是否展示',default=True)

    def __str__(self):
        return self.title

    def get_first_id(self):
        if self.chapter_set.exists():
            return self.chapter_set.order_by('order','id').first().id
        return None

    class Meta:
        verbose_name = "主题"
        verbose_name_plural = verbose_name
        ordering = ['reproduce','id','create_date']


# 定义md文件上传路径
def subject_directory_path(instance, filename):
    return os.path.join('subject', instance.topic.title, filename)


class Chapter(models.Model):
    title = models.CharField('标题', help_text='标题', max_length=64)
    topic = models.ForeignKey(Topic, verbose_name='主题', help_text='所属主题')
    md5 = models.CharField(max_length=128, verbose_name="MD5值")
    md_body = models.TextField('md正文', help_text='正文.md')
    md_File = models.FileField('正文md文件', help_text='md文件', upload_to=subject_directory_path)
    create_date = models.DateTimeField('创建时间', auto_now_add=True, help_text='创建时间')

    order = models.PositiveIntegerField('顺序',default=0)


    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'topic')
        verbose_name = '章节'
        verbose_name_plural = verbose_name
        ordering = ['order','id']
