# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-11-07 21:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import subject.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='标题', max_length=32, verbose_name='标题')),
                ('md5', models.CharField(max_length=128, verbose_name='MD5值')),
                ('md_body', models.TextField(help_text='正文.md', verbose_name='md正文')),
                ('md_File', models.FileField(help_text='md文件', upload_to=subject.models.subject_directory_path, verbose_name='正文md文件')),
                ('create_date', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '章节',
                'verbose_name_plural': '章节',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='标题', max_length=32, unique=True, verbose_name='标题')),
                ('urltag', models.CharField(help_text='标签', max_length=32, unique=True, verbose_name='utag')),
                ('reproduce', models.BooleanField(default=False, help_text='是否转载', verbose_name='是否转载')),
                ('reproduce_source', models.URLField(blank=True, help_text='转载来源地址', max_length=512, null=True, verbose_name='转载来源地址')),
                ('create_date', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('desc', models.TextField(default='', help_text='主题描述', max_length=200, verbose_name='主题描述')),
                ('img', models.ImageField(blank=True, null=True, upload_to='subject/topic/', verbose_name='图片')),
            ],
            options={
                'verbose_name': '主题',
                'verbose_name_plural': '主题',
            },
        ),
        migrations.AddField(
            model_name='chapter',
            name='topic',
            field=models.ForeignKey(help_text='所属主题', on_delete=django.db.models.deletion.CASCADE, to='subject.Topic', verbose_name='主题'),
        ),
        migrations.AlterUniqueTogether(
            name='chapter',
            unique_together=set([('title', 'topic')]),
        ),
    ]