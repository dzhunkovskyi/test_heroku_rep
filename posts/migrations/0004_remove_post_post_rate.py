# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 18:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_post_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_rate',
        ),
    ]