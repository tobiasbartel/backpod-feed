from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.db import models
import logging
logger = logging.getLogger(__name__)


class Category(models.Model):
    title = models.CharField(max_length=250, db_index=True)
    created = models.DateTimeField(editable=False, auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True, db_index=True)

    def __unicode__(self):
        return u'%s' % self.title


class Itunes_category(models.Model):
    title = models.CharField(max_length=250, db_index=True)
    created = models.DateTimeField(editable=False, auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True, db_index=True)

    def __unicode__(self):
        return u'%s' % self.title

class PodcastCategory(models.Model):
    title = models.CharField(max_length=250, db_index=True)
    created = models.DateTimeField(editable=False, auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True, db_index=True)

    def __unicode__(self):
        return u'%s' % self.title

class Itunes_keyword(models.Model):
    keyword = models.CharField(max_length=250, db_index=True)
    created = models.DateTimeField(editable=False, auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True, db_index=True)

    def __unicode__(self):
        return u'%s' % self.title

class Person(models.Model):
    name = models.CharField(max_length=250, db_index=True, blank=True, null=True)
    lower_name = models.CharField(max_length=250, db_index=True, blank=True, null=True)
    email = models.EmailField(max_length=250, db_index=True, blank=True, null=True)
    is_author = models.BooleanField(default=False)
    is_itunes_author = models.BooleanField(default=False)
    is_managing_editor = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    is_webmaster = models.BooleanField(default=False)
    created = models.DateTimeField(editable=False, auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        unique_together = (('lower_name', 'email', ),)

    def __unicode__(self):
        return u'%s' % self.name


class Language(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    created = models.DateTimeField(editable=False, auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True, db_index=True)

    def __unicode__(self):
        return u'%s' % self.name


class Feed(models.Model):
    url = models.URLField(default=None, null=True, db_index=True)
    itunes_id = models.BigIntegerField(db_index=True)
    categories = models.ManyToManyField('PodcastCategory', blank=True, related_name='podcast_category')
    itunes_directory = models.ForeignKey('directory.Itunes', blank=True, db_index=True)
    copyright = models.CharField(max_length=250, blank=True, null=True)
    creative_commons = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    generator = models.CharField(max_length=250, blank=True, null=True)
    image_title = models.CharField(max_length=250, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    image_link = models.URLField(blank=True, null=True)
    itunes_author_name = models.ForeignKey(Person, related_name="feed_itunes_author_name", blank=True, null=True)
    itunes_block = models.NullBooleanField(default=False, blank=True, null=True)
    itunes_categories = models.ManyToManyField(Itunes_category, blank=True)
    itunes_complete = models.CharField(max_length=250, blank=True, null=True)
    itunes_explicit = models.CharField(max_length=250, blank=True, null=True)
    itunes_image = models.URLField(blank=True, null=True)
    itunes_keywords = models.ManyToManyField(Itunes_keyword, blank=True)
    itunes_new_feed_url = models.URLField(blank=True, null=True)
    language = models.ForeignKey(Language, related_name="feed_language", blank=True, null=True)
    last_build_date = models.DateTimeField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    managing_editor = models.ForeignKey(Person, related_name="feed_managing_director", blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    pubsubhubbub = models.URLField(blank=True, null=True)
    owner = models.ForeignKey(Person, related_name="feed_owner_name", blank=True, null=True)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    ttl = models.IntegerField(blank=True, null=True)
    web_master = models.ForeignKey(Person, related_name="feed_web_master", blank=True, null=True)
    time_published = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(editable=False, auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        unique_together = (('url', 'itunes_id', ),)

    def __unicode__(self):
        return u'%s' % self.title


class Item(models.Model):
    object_hash = models.CharField(max_length=50, db_index=True)
    feed = models.ForeignKey(Feed, related_name='item_from_feed', db_index=True, blank=True, null=True)
    author = models.ForeignKey(Person, related_name="item_author", blank=True, null=True)
    comments = models.URLField(blank=True, null=True)
    creative_commons = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    enclosure_url = models.URLField(blank=True, null=True, db_index=True)
    enclosure_type = models.CharField(max_length=250, blank=True, null=True)
    enclosure_length = models.CharField(max_length=250, blank=True, null=True)
    guid = models.CharField(max_length=250, blank=True, null=True, db_index=True)
    itunes_author_name = models.ForeignKey(Person, related_name="item_itunes_author_name", blank=True, null=True)
    itunes_block = models.NullBooleanField(default=False, blank=True, null=True)
    itunes_closed_captioned = models.CharField(max_length=250, blank=True, null=True)
    itunes_duration = models.CharField(max_length=250, blank=True, null=True)
    itunes_explicit = models.CharField(max_length=250, blank=True, null=True)
    itunes_image = models.URLField(blank=True, null=True)
    itunes_order = models.CharField(max_length=250, blank=True, null=True)
    itunes_subtitle = models.TextField(blank=True, null=True)
    itunes_summary = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    time_published = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(editable=False, auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        unique_together = (('object_hash', 'time_published', ),)

    def __unicode__(self):
        return u'%s' % self.title
