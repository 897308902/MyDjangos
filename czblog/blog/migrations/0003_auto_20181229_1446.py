# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-29 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181229_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('1', '\u7537'), ('0', '\u5973')], default='female', max_length=6, verbose_name='\u6027\u522b'),
        ),
    ]
