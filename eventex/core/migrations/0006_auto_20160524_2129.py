# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-24 21:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_talk'),
    ]

    operations = [
        migrations.RenameField(
            model_name='talk',
            old_name='speaker',
            new_name='speakers',
        ),
    ]