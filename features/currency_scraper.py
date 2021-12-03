from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def get_prices():
    try:
        with webdriver.Firefox() as driver:
            driver.get('https://www.tgju.org/currency')
            time.sleep(10)
            rows = driver.find_elements(By.CLASS_NAME, 'pointer')
            rows += driver.find_elements(By.CLASS_NAME, 'tr-low')
            rows += driver.find_elements(By.CLASS_NAME, 'tr-high')
            rows += driver.find_elements(By.CLASS_NAME, 'row-.tr-')
            currency_prices = {}

            for row in rows:
                name = row.find_element(By.TAG_NAME, 'th').text
                price = row.find_element(By.TAG_NAME, 'td').text
                price = price.split(',')
                price = ''.join(price)
                price = int(price)
                currency_prices[name] = price

            return currency_prices
    except:
        return None


get_prices()
