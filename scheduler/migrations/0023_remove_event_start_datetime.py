# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 03:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0022_auto_20160430_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='start_datetime',
        ),
    ]
