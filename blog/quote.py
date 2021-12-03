import requests
from bs4 import BeautifulSoup


def scrape_quote():
    """returns a quote dictionary scraped from www.time.ir that contains quote and quote_author.
    if the quote is a not formatted in a single html tag (like poetries), it makes another request
    and will get another quote. see time.ir for understanding how the quote is represented.
    in case of connection errors related to requests library it will return None."""

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
            quote['identifier'] = f"{quote['quote_author']}_{quote['quote'][0:5]}_{quote['quote'][-7:-1]}"
            return quote

    except requests.exceptions.RequestException:
        return None
