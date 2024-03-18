import logging
from dotenv import load_dotenv
import os
import requests
from forex_python.converter import CurrencyCodes

logging.basicConfig(level=logging.INFO)

load_dotenv()
api_key = os.getenv('EXCHANGE_RATES_API_KEY')


def get_latest_rates(additionalSymbols, access_key=api_key):
    endpoint = 'latest'
    url = f'http://api.exchangeratesapi.io/v1/{endpoint}?access_key={access_key}&symbols=ILS, USD, EUR, {additionalSymbols}'

    response = requests.get(url)
    logging.info(f"Request to {url} returned {response.status_code}")
    exchange_rates = response.json()
    return exchange_rates


def is_valid_currency_symbol(symbol):
    currency_codes = CurrencyCodes()
    return currency_codes.get_symbol(symbol) is not None


# Example usage
if __name__ == "__main__":
    print(get_latest_rates('USD'))
