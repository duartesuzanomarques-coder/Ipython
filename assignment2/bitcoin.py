# Bitcoin Price Index - CS50P Problem Set 4

import sys
import requests

API_KEY = "YOUR_API_KEY"
URL = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"


def main():
    n = get_amount(sys.argv)
    price = get_price()
    # Thousands separator and 4 decimal places
    print(f"${n * price:,.4f}")


def get_amount(argv):
    """Read the number of bitcoins from the command line."""
    if len(argv) < 2:
        sys.exit("Missing command-line argument")
    try:
        return float(argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")


def get_price():
    """Query the CoinCap API and return the current BTC price in USD."""
    try:
        response = requests.get(URL)
        # Nested JSON: the price is a string inside data -> priceUsd
        return float(response.json()["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Could not reach the CoinCap API")


if __name__ == "__main__":
    main()
