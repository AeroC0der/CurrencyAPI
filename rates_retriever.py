import logging
from dotenv import load_dotenv
import os
import requests
from forex_python.converter import CurrencyCodes

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load environment variables
load_dotenv()
api_key = os.getenv('EXCHANGE_RATES_API_KEY')


def get_latest_rates(additionalSymbols, access_key=api_key):
    """
    Retrieves the latest exchange rates for a set of specified currency symbols.

    :param additionalSymbols: A string containing additional currency symbols separated by commas (baseCurrency loop-hole).
    :param access_key: The API key for accessing the Exchange Rates API.
    :return: A dictionary containing the latest exchange rates.
    """
    endpoint = 'latest'
    url = f'http://api.exchangeratesapi.io/v1/{endpoint}?access_key={access_key}&symbols=ILS,USD,EUR,{additionalSymbols}'

    response = requests.get(url)
    logging.info(f"Request to {url} returned {response.status_code}")
    exchange_rates = response.json()
    return exchange_rates


def is_valid_currency_symbol(symbol):
    """
    Checks if the provided symbol is a valid currency symbol.

    :param symbol: The currency symbol to validate.
    :return: True if the symbol is valid, False otherwise.
    """
    currency_codes = CurrencyCodes()
    return currency_codes.get_symbol(symbol) is not None


# Example usage
if __name__ == "__main__":
    print(get_latest_rates('USD'))
