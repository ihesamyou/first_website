from celery import shared_task
from .currency_scraper import get_prices
from .models import Currency


@shared_task
def update_prices():
    prices = get_prices()

    if prices:
        for name, price in prices.items():
            old_price = Currency.objects.get(name=name)
            old_price.price = price
            old_price.save()
