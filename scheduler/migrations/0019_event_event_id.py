# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 01:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0018_auto_20160430_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_id',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 1, 1, 42, 13, 788000, tzinfo=utc)),
        ),
    ]
