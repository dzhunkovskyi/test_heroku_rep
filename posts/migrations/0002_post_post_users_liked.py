# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_users_liked',
            field=models.CharField(default='[]', max_length=200),
        ),
    ]
