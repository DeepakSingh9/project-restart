# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-23 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20171106_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, default='static/images/blankprofile.jpg', upload_to='blogimages/pic'),
        ),
    ]
