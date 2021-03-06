# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-10-09 02:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_auto_20191004_0216'),
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.PositiveIntegerField(choices=[(0, '未作选择'), (1, '赞同'), (2, '反对')], default=0)),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('post', models.ForeignKey(help_text='文章id', on_delete=django.db.models.deletion.CASCADE, to='blog.Post', verbose_name='文章')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户投票',
                'verbose_name_plural': '用户投票',
            },
        ),
        migrations.AlterUniqueTogether(
            name='uservote',
            unique_together=set([('user', 'post')]),
        ),
    ]
