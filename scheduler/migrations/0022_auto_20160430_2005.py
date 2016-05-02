# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0021_auto_20160430_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='id',
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False, unique=True),
        ),
    ]