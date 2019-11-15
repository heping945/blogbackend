import uuid
import os

from django.db import models

# Create your models here.


# 定义图片上传路径
def img_directory_path(instance, filename):
    # 取上传文件类型
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(instance.name, ext)
    sub_folder = 'img'
    return os.path.join('postserver', sub_folder, filename)


class PostImg(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    name=models.CharField('文件名',max_length=64,help_text='文件名')
    imgMd5 = models.CharField(max_length=128, verbose_name="MD5值")
    img = models.ImageField('图片', help_text='图片',upload_to=img_directory_path)
    created_time = models.DateTimeField('创建时间', auto_now_add=True, help_text='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "文章图片"
        verbose_name_plural = verbose_name
