from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Info(models.Model):
    title = models.CharField('标题', max_length=200, unique=True, help_text='标题')
    body = RichTextField('正文', help_text='正文',null=True,blank=True)
    body_md = models.TextField('正文.md', help_text='正文.md', null=True, blank=True)
    create_date = models.DateTimeField('创建时间',auto_now_add=True,help_text='创建时间')
    mod_date = models.DateTimeField('修改时间',auto_now=True,help_text='修改时间')

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-create_date']
        verbose_name = "信息"
        verbose_name_plural = verbose_name
