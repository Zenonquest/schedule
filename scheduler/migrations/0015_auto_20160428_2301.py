# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 05:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0014_auto_20160428_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='start_date',
            field=models.DateField(default=datetime.date(2016, 4, 29), verbose_name='start date'),
        ),
    ]
