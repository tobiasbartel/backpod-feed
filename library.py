import hashlib
from datetime import datetime
from pprint import pprint

import dateutil.parser
import requests
from pyPodcastParser.Podcast import Podcast

from directory.models import Itunes
from models import *


def handle_categories(my_categories):
    list_of_categories = []
    for item in my_categories:
        db_category, created = PodcastCategory.objects.get_or_create(title=item.lower().strip())
        list_of_categories.append(db_category)
    return list_of_categories


def handle_itunes_categories(my_categories):
    list_of_itunes_categories = []
    for item in my_categories:
        itunes_category, created = Itunes_category.objects.get_or_create(title=item.lower().strip())
        list_of_itunes_categories.append(itunes_category)
    return list_of_itunes_categories


def handle_itunes_keywords(my_keywords):
    list_of_itunes_keywords = []
    for item in my_keywords:
        itunes_keyword, created = Itunes_keyword.objects.get_or_create(keyword=item.lower().strip())
        list_of_itunes_keywords.append(itunes_keyword)
    return list_of_itunes_keywords


def handle_person(my_name, my_mail_address=None, my_type=None):
    if my_type is None:
        return None

    if my_name is None:
        my_lower_name = None
    else:
        my_name = my_name.strip()
        my_lower_name = my_name.lower().strip()

    if my_mail_address is not None:
        my_mail_address = my_mail_address.lower().strip()

    changed = False
    if my_type == 'owner':
        db_person, created = Person.objects.get_or_create(lower_name=my_lower_name, email=my_mail_address)
    else:
        db_person, created = Person.objects.get_or_create(lower_name=my_lower_name)

    if db_person.name != my_name:
        db_person.name = my_name
        changed = True
    if not db_person.is_author and my_type == 'author':
        db_person.is_itunes_author = True
        changed = True
    if not db_person.is_itunes_author and my_type == 'itunes_author':
        db_person.is_itunes_author = True
        changed = True
    if not db_person.is_managing_editor and my_type == 'managing_editor':
        db_person.is_managing_editor = True
        changed = True
    if not db_person.is_owner and my_type == 'owner':
        db_person.is_managing_editor = True
        changed = True
    if not db_person.is_owner and my_type == 'webmaster':
        db_person.is_webmaster = True
        changed = True

    if changed:
        db_person.save()

    return db_person


def handle_language(my_language):
    db_language, created = Language.objects.get_or_create(name=my_language)
    return db_language


def import_feed_from_itunes(feed_url, collection_id):
    pprint(feed_url)
    response = requests.get(feed_url)
    podcast = Podcast(response.content)
    itunes_object = Itunes.objects.get(collection_id=collection_id)

    try:
        published_date = dateutil.parser.parse(podcast.published_date)
    except:
        published_date = None

    try:
        last_build_date = dateutil.parser.parse(podcast.last_build_date)
    except:
        last_build_date = None

    my_feed, created = Feed.objects.get_or_create(url=feed_url, itunes_directory=itunes_object,
                                                  itunes_id=itunes_object.collection_id)
    pprint(created)
    pprint(my_feed)
    pprint(podcast)

    if podcast.owner_name is None:
        podcast.owner_name = ''

    my_feed.owner = handle_person(podcast.owner_name, podcast.owner_email, 'owner')

    my_feed.categories = handle_categories(podcast.categories)
    my_feed.itunes_directory = itunes_object
    my_feed.copyright = podcast.copyright
    my_feed.creative_commons = podcast.creative_commons
    my_feed.description = podcast.description
    my_feed.generator = podcast.generator
    my_feed.image_title = podcast.image_title
    my_feed.image_url = podcast.image_url
    my_feed.image_link = podcast.image_link
    my_feed.itunes_author_name = handle_person(my_name=podcast.itunes_author_name, my_type='itunes_author')
    my_feed.itunes_block = podcast.itunes_block
    my_feed.itunes_categories = handle_itunes_categories(podcast.itunes_categories  )
    my_feed.itunes_complete = podcast.itunes_complete
    my_feed.itunes_explicit = podcast.itunes_explicit
    my_feed.itunes_image = podcast.itune_image
    my_feed.itunes_keywords = handle_itunes_keywords(podcast.itunes_keywords)
    my_feed.itunes_new_feed_url = podcast.itunes_new_feed_url
    my_feed.language = handle_language(podcast.language)
    my_feed.last_build_date = last_build_date
    my_feed.link = podcast.link
    my_feed.managing_editor = handle_person(my_name=podcast.managing_editor, my_type='managing_editor')
    my_feed.published_date = published_date
    my_feed.pubsubhubbub = podcast.pubsubhubbub
    my_feed.subtitle = podcast.subtitle
    my_feed.title = podcast.title
    if my_feed.ttl is not None:
        my_feed.ttl = int(podcast.ttl)
    my_feed.web_master = handle_person(my_name=podcast.web_master, my_type='webmaster')
    if my_feed.time_published is not None:
        my_feed.time_published = datetime.fromtimestamp(float(podcast.time_published))
    my_feed.save()

    for my_item in podcast.items:
        import_feed_item(my_feed=my_feed, my_item=my_item)

def import_feed_item(my_feed, my_item):
    pprint(my_item)

    my_hash = hashlib.sha1('%s-%s-%s' % (my_item.enclosure_url, my_feed.pk, my_item.guid)).hexdigest()
    pprint(my_hash)
    if my_item.time_published is not None:
        my_published_date = datetime.fromtimestamp(float(my_item.time_published))
    else:
        my_published_date = datetime.fromtimestamp(0)

    pprint(my_published_date)
    my_feed_item, created = Item.objects.get_or_create(object_hash=my_hash, time_published=my_published_date)

    my_item.author = handle_person(my_name=my_item.author, my_type='author')
    my_feed_item.comments = my_item.comments
    my_feed_item.creative_commons = my_item.creative_commons
    my_feed_item.description = my_item.description
    my_feed_item.enclosure_url = my_item.enclosure_url
    my_feed_item.enclosure_type = my_item.enclosure_type
    my_feed_item.enclosure_length= my_item.enclosure_length
    my_feed_item.guid = my_item.guid
    my_feed_item.itunes_author_name = handle_person(my_name=my_item.itunes_author_name, my_type='itunes_author')
    my_feed_item.itunes_block = my_item.itunes_block
    my_feed_item.itunes_closed_captioned = my_item.itunes_closed_captioned
    my_feed_item.itunes_duration = my_item.itunes_duration
    my_feed_item.itunes_explicit = my_item.itunes_explicit
    my_feed_item.itunes_image = my_item.itune_image
    my_feed_item.itunes_order = my_item.itunes_order
    my_feed_item.itunes_subtitle = my_item.itunes_subtitle
    my_feed_item.itunes_summary = my_item.itunes_summary
    my_feed_item.link = my_item.link
    my_feed_item.title = my_item.title
    my_feed_item.time_published = my_published_date
    my_feed_item.save()
