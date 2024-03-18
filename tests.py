import pytest
import requests

# Define the base URL of the currency check service
BASE_URL = "http://localhost:8000/check-currency"

# Test data with different thresholds and base currencies
# The expected responses only include "NIS", "EUR", and "USD", excluding the base currency
test_data = [
    ("USD", 1.2, {"NIS": True, "EUR": False}),
    ("EUR", 0.8, {"NIS": True, "USD": True}),
    ("JPY", 0.5, {"NIS": False, "EUR": False, "USD": False}),
    ("GBP", 1.5, {"NIS": True, "EUR": False, "USD": False}),
    ("CAD", 0.75, {"NIS": True, "EUR": False, "USD": False}),
    ("AUD", 1.1, {"NIS": True, "EUR": False, "USD": False}),
    ("CHF", 1.3, {"NIS": True, "EUR": False, "USD": False}),
    ("CNY", 0.15, {"NIS": True, "EUR": False, "USD": False}),
    ("SEK", 0.1, {"NIS": True, "EUR": False, "USD": False}),
    ("NZD", 0.6, {"NIS": True, "EUR": False, "USD": True}),
    ("NIS", 1.0, {"EUR": False, "USD": False}),
    ("ILS", 2.0, {"EUR": False, "USD": False}),
]


@pytest.mark.parametrize("base_currency, threshold, expected_response", test_data)
def test_check_currency(base_currency, threshold, expected_response):
    # Construct the request URL with the provided parameters
    url = f"{BASE_URL}?threshold={threshold}&baseCurrency={base_currency}"

    # Send the GET request to the service
    response = requests.get(url)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response JSON matches the expected response
    assert response.json() == expected_response


def test_check_missing_parameters():
    # Send a GET request without the required parameters
    response = requests.get(BASE_URL)

    # Assert that the response status code is 400 (Bad Request)
    assert response.status_code == 400

    # Assert that the response JSON contains the expected error message
    assert response.json() == {'error': 'Missing required parameters'}


def test_check_invalid_currency_symbol():
    # Send a GET request with an invalid currency code
    response = requests.get(f"{BASE_URL}?threshold=1.0&baseCurrency=XYZ")

    # Assert that the response status code is 400 (Bad Request)
    assert response.status_code == 400

    # Assert that the response JSON contains the expected error message
    assert response.json() == {'error': 'Invalid currency symbol'}


if __name__ == "__main__":
    pytest.main()
