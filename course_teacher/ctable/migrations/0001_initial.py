# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-03 22:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, unique=True)),
                ('period', models.IntegerField(db_index=True)),
                ('description', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=50, unique=True)),
                ('gender', models.IntegerField()),
                ('address', models.CharField(max_length=50, null=True)),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course', to='ctable.Course')),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
    ]
