# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-11-07 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(help_text='标题', max_length=64, unique=True, verbose_name='标题'),
        ),
    ]