# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 23:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0011_auto_20160925_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='lower_name',
            field=models.CharField(blank=True, db_index=True, max_length=250, null=True),
        ),
    ]