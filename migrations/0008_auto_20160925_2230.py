# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 22:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_auto_20160925_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='itunes_block',
            field=models.NullBooleanField(default=False),
        ),
    ]
