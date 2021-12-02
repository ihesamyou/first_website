import requests
from bs4 import BeautifulSoup


def get_quote():
    """returns a quote dictionary scraped from www.time.ir that may contain
    quote and quote_author or error_message for connection errors related to requests library.
    if the quote is a not formatted in a single html tag, it makes another request
    and will get another quote. see time.ir for understanding how the quote is represented.
    can't scrape poetries."""

    quote = {}
    try:
        data = requests.get('https://www.time.ir/').text
        soup = BeautifulSoup(data, 'lxml')
        random_quote = soup.find('div', class_='randomQuote')
        if random_quote.span.contents[0].next_sibling:
            return get_quote()
        else:
            quote['quote'] = random_quote.span.text
            quote['quote_author'] = random_quote.div.a.text
            return quote
    except requests.exceptions.RequestException:
        quote['error_message'] = 'در حال حاضر مشکلی برای بخش نقل قول به وجود آمده است.'
        return quote
