from flask import Flask, request, jsonify
from rates_retriever import get_latest_rates, is_valid_currency_symbol
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create a Flask application
app = Flask(__name__)


@app.route('/')
def hello_world():
    """
    A simple route to check if the API is working.
    :return: A message indicating that the API is working.
    """
    return 'API is working!'


@app.route('/check-currency')
def check_currency():
    """
    Checks if the exchange rates of other currencies compared to the base currency are above a certain threshold.
    :return: A JSON object containing the currencies and whether their exchange rates meet the threshold (bool).
    """
    threshold = request.args.get('threshold', type=float)
    baseCurrency = request.args.get('baseCurrency', type=str)

    # Validate input parameters
    if threshold is None or baseCurrency is None:
        return jsonify({'error': 'Missing required parameters'}), 400

    # Convert NIS to ILS for exchangeratesapi.io API
    if baseCurrency == 'NIS':
        baseCurrency = 'ILS'

    if is_valid_currency_symbol(baseCurrency) is False:
        return jsonify({'error': 'Invalid currency symbol'}), 400

    # Retrieve exchange rates from the API
    logging.info("Retrieving exchange rates from the API...")
    exchange_rate = get_latest_rates(baseCurrency)
    logging.info(f"Request to {baseCurrency} returned {exchange_rate}")

    if exchange_rate is None:
        return jsonify({'error': 'Invalid currency code'}), 400

    # Process the exchange rates
    base_rate = exchange_rate['rates'][baseCurrency]
    response_output = {}
    for symbol, rate in exchange_rate['rates'].items():
        if symbol != baseCurrency:
            if symbol == 'ILS':
                symbol = 'NIS'
            # Normalizing the rates to the base currency
            response_output[symbol] = (rate / base_rate >= threshold)

    return jsonify(response_output)


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, port=8000)


# For creating a test client
def create_app():
    return app
