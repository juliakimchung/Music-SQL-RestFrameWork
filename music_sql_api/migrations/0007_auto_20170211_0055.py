# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 00:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_sql_api', '0006_auto_20170211_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.DateField(default=0),
        ),
    ]
