from django.db import models
from ckeditor.fields import RichTextField
from unidecode import unidecode
from django.template.defaultfilters import slugify


# from operation.models import UserVote
from  .utils import makexcerpt
from  accounts.models import UserProfile
# Create your models here.

class Category(models.Model):
    """文章分类"""
    name = models.CharField('分类名', max_length=30, unique=True)
    slug = models.SlugField('slug', max_length=40,blank=True)
    parent_category = models.ForeignKey('self', verbose_name="父级分类", blank=True, null=True,related_name='sub_cat')

    def get_absolute_url(self):
        return '/api/v1/categories/'+self.slug

    def get_post_count(self):
        return Post.objects.filter(category__slug=self.slug).count()

    def has_child(self):
        if self.sub_cat.all().count() > 0:
            return True

    def save(self, *args, **kwargs):
        if not self.id or not self.slug:
            # Newly created object, so set slug
            self.slug = slugify(unidecode(self.name[:8]))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "分类"
        verbose_name_plural = verbose_name


class Post(models.Model):
    '''文章模型'''
    title = models.CharField('标题',max_length=200,unique=True,help_text='标题')
    body = RichTextField('正文',help_text='正文')
    body_md = models.TextField('正文.md',help_text='正文.md',null=True,blank=True)
    excerpt = models.CharField('摘要',max_length=200, blank=True,help_text='摘要')
    codestyle = models.CharField('代码风格',max_length=24,help_text='md代码风格',blank=True,null=True,default='monokai')
    reproduce = models.BooleanField('是否转载',default=False,help_text='是否转载')
    reproduce_source = models.URLField('转载来源地址',max_length=512,null=True,blank=True,help_text='转载来源地址')
    create_date = models.DateTimeField('创建时间',auto_now_add=True,help_text='创建时间')
    mod_date = models.DateTimeField('修改时间',auto_now=True,help_text='修改时间')
    views_count = models.PositiveIntegerField('浏览量',default=0,help_text='浏览量')
    can_comment = models.BooleanField('是否可以评论',default=True,help_text='是否可以评论')
    comment_count = models.PositiveIntegerField('评论数',default=0,help_text='评论数')
    upvote_count = models.IntegerField ('点赞数',default=0,help_text='点赞数')
    ifshow = models.BooleanField('是否展示', default=True)

    author = models.ForeignKey(UserProfile,verbose_name='作者',help_text='文章作者')
    category = models.ForeignKey('Category', verbose_name='分类', blank=False, null=False,help_text='文章分类',related_name='cat_post')
    tags = models.ManyToManyField('Tag', verbose_name='标签', blank=True,help_text='文章标签')


    def __str__(self):
        return self.title


    def viewed(self):
        self.views_count += 1
        self.save(update_fields=['views_count'])

    # 返回评论数量
    def get_post_comment_count(self):
        return self.post_comments.all().count()

    def save(self, *args, **kwargs):
        # 从 body 摘取前 150 个字符赋给到 excerpt
        self.excerpt = makexcerpt(self.body)[:150]
        # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)

    # def get_post_upvote_count(self):
    #     return Post.objects.filter(uservote__post__id=self.id).count()

    class Meta:
        ordering = ['-create_date']
        verbose_name = "文章"
        verbose_name_plural = verbose_name



class Tag(models.Model):
    """文章标签"""
    name = models.CharField('标签名', max_length=30, unique=True)
    slug = models.SlugField('slug', max_length=124,blank=True)
    # author = models.ForeignKey(UserProfile, verbose_name='作者', help_text='文章作者',null=True,blank=True)


    def __str__(self):
        return self.name


    def get_post_count(self):
        return Post.objects.filter(tags__slug=self.slug).count()

    def save(self, *args, **kwargs):
        if not self.id or not self.slug:
            # Newly created object, so set slug
            self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)
    class Meta:
        ordering = ['name']
        verbose_name = "标签"
        verbose_name_plural = verbose_name
