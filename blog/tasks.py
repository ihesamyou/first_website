from blog.models import Quote
from celery import shared_task
from .quote import scrape_quote
import random
from django.core.cache import cache


@shared_task
def get_quote():
    quote_obj = scrape_quote()

    if quote_obj and not Quote.objects.filter(identifier=quote_obj['identifier']):
        Quote.objects.create(
            quote=quote_obj['quote'], author=quote_obj['quote_author'], identifier=quote_obj['identifier'])


@shared_task
def random_quote():
    items = Quote.objects.all()
    quote = random.choice(items)
    cache.set('quote', quote, 310)
