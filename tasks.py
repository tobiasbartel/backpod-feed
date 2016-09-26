from celery import task

from feed.library import import_feed_from_itunes


@task(name="import_feed_from_itunes_task")
def import_feed_from_itunes_task(feed_url, itunes):
    return import_feed_from_itunes(feed_url, itunes)
