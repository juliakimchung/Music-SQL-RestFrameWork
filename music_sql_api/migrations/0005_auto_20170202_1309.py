# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 13:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_sql_api', '0004_auto_20170202_1254'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='albumsong',
            options={'ordering': ('album',)},
        ),
    ]
