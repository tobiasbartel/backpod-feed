import logging

from django.core.management.base import BaseCommand

from directory.models import Itunes
from feed.library import import_feed_from_itunes
from feed.tasks import import_feed_from_itunes_task
from main.settings import DEBUG

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        for one_podcast in Itunes.objects.all().order_by('-modified'):
            if DEBUG:
                logger.info('Updating \'%s\'' % one_podcast)
                import_feed_from_itunes(one_podcast.feed_url, one_podcast.collection_id)
            else:
                import_feed_from_itunes_task.delay(one_podcast.feed_url, one_podcast.collection_id)
