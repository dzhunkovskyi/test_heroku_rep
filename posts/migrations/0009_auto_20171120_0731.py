# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_comments_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_image',
        ),
        migrations.AddField(
            model_name='post',
            name='post_image_url',
            field=models.CharField(default='', max_length=400),
        ),
    ]
