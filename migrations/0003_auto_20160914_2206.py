# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-14 22:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_feed_itunes_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feed',
            old_name='itunes_id',
            new_name='itunes_directory',
        ),
    ]
