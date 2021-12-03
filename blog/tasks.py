from blog.models import Quote
from celery import shared_task
from .quote import get_quote


@shared_task
def quote_task():
    quote_obj = get_quote()

    if quote_obj and not Quote.objects.filter(identifier=quote_obj['identifier']):
        Quote.objects.create(
            quote=quote_obj['quote'], author=quote_obj['quote_author'], identifier=quote_obj['identifier'])
