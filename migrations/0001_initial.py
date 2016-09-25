# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-14 19:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copyright', models.CharField(blank=True, max_length=250, null=True)),
                ('creative_commons', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('generator', models.CharField(blank=True, max_length=250, null=True)),
                ('image_title', models.CharField(blank=True, max_length=250, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('image_link', models.URLField(blank=True, null=True)),
                ('itunes_block', models.BooleanField()),
                ('itunes_complete', models.CharField(blank=True, max_length=250, null=True)),
                ('itunes_explicit', models.CharField(blank=True, max_length=250, null=True)),
                ('itunes_image', models.URLField(blank=True, null=True)),
                ('itunes_new_feed_url', models.URLField(blank=True, null=True)),
                ('last_build_date', models.DateTimeField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('pubsubhubbub', models.URLField(blank=True, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=250, null=True)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('ttl', models.IntegerField(blank=True, null=True)),
                ('date_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True, null=True)),
                ('creative_commons', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('enclosure_url', models.URLField(blank=True, null=True)),
                ('enclosure_type', models.CharField(blank=True, max_length=250, null=True)),
                ('enclosure_length', models.CharField(blank=True, max_length=250, null=True)),
                ('guid', models.CharField(blank=True, max_length=250, null=True)),
                ('itunes_closed_caption', models.CharField(blank=True, max_length=250, null=True)),
                ('itunes_duration', models.TimeField(blank=True, null=True)),
                ('itunes_explicit', models.CharField(blank=True, max_length=250, null=True)),
                ('itunes_image', models.URLField(blank=True, null=True)),
                ('itunes_order', models.CharField(blank=True, max_length=250, null=True)),
                ('itunes_subtitle', models.TextField(blank=True, null=True)),
                ('itunes_summary', models.TextField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('date_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Itunes_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Itunes_keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(db_index=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=250)),
                ('email', models.EmailField(db_index=True, max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fitem_author', to='feed.Person'),
        ),
        migrations.AddField(
            model_name='item',
            name='itunes_author_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_itunes_author_name', to='feed.Person'),
        ),
        migrations.AddField(
            model_name='feed',
            name='itunes_author_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feed_itunes_author_name', to='feed.Person'),
        ),
        migrations.AddField(
            model_name='feed',
            name='itunes_categories',
            field=models.ManyToManyField(blank=True, to='feed.Itunes_category'),
        ),
        migrations.AddField(
            model_name='feed',
            name='itunes_keywords',
            field=models.ManyToManyField(blank=True, to='feed.Itunes_keyword'),
        ),
        migrations.AddField(
            model_name='feed',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feed_language', to='feed.Language'),
        ),
        migrations.AddField(
            model_name='feed',
            name='managing_editor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feed_managing_director', to='feed.Person'),
        ),
        migrations.AddField(
            model_name='feed',
            name='owner_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feed_owner_name', to='feed.Person'),
        ),
        migrations.AddField(
            model_name='feed',
            name='web_master',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feed_web_master', to='feed.Person'),
        ),
    ]
