# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20161020_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_resized',
            field=models.BooleanField(default=False),
        ),
    ]
