from flask import Flask, request, jsonify
from rates_retriever import get_latest_rates, is_valid_currency_symbol
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'API is working!'


@app.route('/check-currency')
def check_currency():
    threshold = request.args.get('threshold', type=float)
    baseCurrency = request.args.get('baseCurrency', type=str)

    if threshold is None or baseCurrency is None:
        return jsonify({'error': 'Missing required parameters'}), 400

    if is_valid_currency_symbol(baseCurrency) is False:
        return jsonify({'error': 'Invalid currency symbol'}), 400

    if baseCurrency == 'NIS':
        baseCurrency = 'ILS'

    # function from rates_retriever.py
    exchange_rate = get_latest_rates(baseCurrency)

    logging.info("Retrieving exchange rates from the API...")
    logging.info(f"Request to {baseCurrency} returned {exchange_rate}")

    if exchange_rate is None:
        return jsonify({'error': 'Invalid currency code'}), 400

    base_rate = exchange_rate['rates'][baseCurrency]
    response_output = {}

    for symbol, rate in exchange_rate['rates'].items():
        if symbol != baseCurrency:
            if symbol == 'ILS':
                symbol = 'NIS'
            # Normalizing the rates to the base currency (default: EUR, to change need to upgrade API subscription)
            response_output[symbol] = (rate/base_rate >= threshold)

    return jsonify(response_output)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
