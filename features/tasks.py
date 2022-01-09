from celery import shared_task
from .currency_scraper import get_prices
from .models import Currency
from django.core.cache import cache
from personal_website.celery import create_connection


@shared_task
def update_prices():
    """
    Updates currency model prices using get_prices function.
    """
    prices = get_prices()

    if prices:
        connection = create_connection()
        for name, price in prices.items():
            try:
                old_price = Currency.objects.get(name=name)
                old_price.price = price
                old_price.save()
                cache.set(name, price, None)
            except Currency.DoesNotExist:
                Currency.objects.create(name=name, price=price)
                cache.set(name, price, None)
        connection.close()
