# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-12 03:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20160620_2052'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='talk',
            options={
                'ordering': ['start'],
                'verbose_name': 'palestra',
                'verbose_name_plural': 'palestras'
            },
        ),
    ]