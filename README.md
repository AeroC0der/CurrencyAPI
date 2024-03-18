# Currency Check Service

This Flask application provides an API for checking if the exchange rates of various currencies compared to a base currency are above a certain threshold.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```

2. Navigate to the project directory:

   ```bash
   cd project-directory
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1.  Start the Flask application:

   ```bash
   python app.py
   ```

2.  The application will be running on [http://localhost:8000]. You can use the following endpoints:

    -   `GET /`: A simple route to check if the API is working.
    -   `GET /check-currency?threshold=<value>&baseCurrency=<currency_code>`: Checks if the exchange rates of other currencies compared to the base currency are above a certain threshold.

    Example:

   ```bash
   curl "http://localhost:8000/check-currency?threshold=1.2&baseCurrency=USD"
   ```

## Testing

To run the tests, execute the following command:

  ```bash
  pytest
  ```

