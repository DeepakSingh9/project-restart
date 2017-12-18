# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-27 07:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20171127_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commented_on', to=settings.AUTH_USER_MODEL),
        ),
    ]
