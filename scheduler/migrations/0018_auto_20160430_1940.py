# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 01:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0017_auto_20160430_1707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_id',
            new_name='id',
        ),
    ]
