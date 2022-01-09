from blog.models import Quote
from celery import shared_task
from .quote import scrape_quote
import random
from django.core.cache import cache

# from personal_website.celery import create_connection


@shared_task
def get_quote():
    """
    This task will get a quote using quote.py and checks if the quote is already in database using identifier.
    if there is a connction problem in the quote.py, it will do nothing.
    """

    quote_obj = scrape_quote()
    # connection = create_connection()
    if quote_obj and not Quote.objects.filter(identifier=quote_obj["identifier"]):
        Quote.objects.create(
            quote=quote_obj["quote"],
            author=quote_obj["quote_author"],
            identifier=quote_obj["identifier"],
        )
    # connection.close()


@shared_task
def random_quote():
    """
    Saves a random quote from Quote model to the cache.
    """
    # connection = create_connection()
    items = Quote.objects.all()
    quote = random.choice(items)
    cache.set("quote", quote.quote, 310)
    cache.set("quote_author", quote.author, 310)
    # connection.close()
