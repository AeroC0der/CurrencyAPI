import logging
from dotenv import load_dotenv
import os
import requests

logging.basicConfig(level=logging.INFO)

load_dotenv()
api_key = os.getenv('EXCHANGE_RATES_API_KEY')


def get_latest_rates(additionalSymbols, access_key=api_key):
    endpoint = 'latest'
    url = f'http://api.exchangeratesapi.io/v1/{endpoint}?access_key={access_key}&symbols=USD, ILS, EUR, {additionalSymbols}'

    response = requests.get(url)
    exchange_rates = response.json()
    return exchange_rates


# Example usage
if __name__ == "__main__":
    print(get_latest_rates('THB'))
