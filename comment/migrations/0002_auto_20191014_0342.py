# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-10-14 03:42
from __future__ import unicode_literals

import comment.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_type', models.PositiveIntegerField(choices=[(1, '留言'), (2, 'bug提交'), (3, '反馈')], default=1, help_text='留言类型: 1(留言),2(bug提交),3(反馈)', verbose_name='留言类型')),
                ('subject', models.CharField(max_length=100, verbose_name='主题')),
                ('content', models.TextField(help_text='留言内容', verbose_name='留言内容')),
                ('file', models.FileField(blank=True, help_text='上传的文件', null=True, upload_to=comment.models.message_directory_path, verbose_name='上传的文件')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_author', to=settings.AUTH_USER_MODEL, verbose_name='信息创建人')),
            ],
            options={
                'verbose_name': '反馈消息',
                'verbose_name_plural': '反馈消息',
            },
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['create_time'], 'verbose_name': '评论', 'verbose_name_plural': '评论'},
        ),
    ]
