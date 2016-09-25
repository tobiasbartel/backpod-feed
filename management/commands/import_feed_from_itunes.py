from django.core.management.base import BaseCommand, CommandError
from feed.library import import_feed_from_itunes
import json
from pprint import pprint
from directory.models import Itunes
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
    	for one_podcast in Itunes.objects.all().order_by('-modified'):
            logger.info('Updating \'%s\'' % one_podcast)
            import_feed_from_itunes(one_podcast.feed_url, one_podcast)