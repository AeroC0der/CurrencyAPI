from flask import Flask, request, jsonify
from rates_retriever import get_latest_rates
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/check-currency')
def check_currency():
    threshold = request.args.get('threshold', type=float)
    baseCurrency = request.args.get('baseCurrency', type=str)

    if threshold is None or baseCurrency is None:
        return jsonify({'error': 'Missing required parameters'}), 400

    # Assuming you have a function to get the exchange rate
    exchange_rate = get_latest_rates(baseCurrency)

    # Switch from EUR perspective to baseCurrency perspective
    exchange_rate = exchange_rate['rates']['USD'] / exchange_rate['rates'][baseCurrency]

    if exchange_rate is None:
        return jsonify({'error': 'Invalid currency code'}), 400

    isMetRate = exchange_rate >= threshold

    return jsonify({
        'currency': baseCurrency,
        'exchange_rate': exchange_rate,
        'meets_threshold': isMetRate
    })


if __name__ == '__main__':
    app.run(debug=True)
