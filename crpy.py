"""
Author: Matheo Alexander
Date: 13.10.2024
Description: This script fetches and displays the latest cryptocurrency data from the CoinMarketCap API.
             It refreshes the data every 30 seconds and displays it in a clean, tabular format with icons for each currency.
                You need to sign up for a free CoinMarketCap API key to use this script.
usage: python crpy.py

"""

import requests
import json
import time
import os

# Dictionary to map currency symbols to icons
currency_icons = {
    'BTC': '₿',
    'ETH': 'Ξ',
    'XRP': '✕',
    'LTC': 'Ł',
    'BCH': 'Ƀ',
    'EOS': 'ε',
    'ADA': '₳',
    'XLM': '★',
    'TRX': 'T',
    'XMR': 'ɱ'
}

# Function to get cryptocurrency data from CoinMarketCap API
def get_crypto_data():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',  # Starting rank of the cryptocurrencies
        'limit': '10',  # Number of cryptocurrencies to retrieve
        'convert': 'USD'  # Convert prices to USD
    }
    headers = {
        'Accepts': 'application/json',  # Accept JSON response
        'X-CMC_PRO_API_KEY': 'your_api_key_here',  # Your CoinMarketCap API key
    }

    # Send GET request to the API
    response = requests.get(url, headers=headers, params=parameters)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        return data
    else:
        print(f"Error: Unable to fetch data (status code: {response.status_code})")
        return None

# Function to display cryptocurrency data
def display_crypto_data(data):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    print(f"{'Icon':<5} {'Name':<20} {'Symbol':<10} {'Price (USD)':<15} {'Market Cap (USD)':<20} {'24h Volume (USD)':<20}")
    print("="*95)
    if 'data' in data:
        for crypto in data['data']:
            name = crypto['name']
            symbol = crypto['symbol']
            icon = currency_icons.get(symbol, '?')  # Get the icon or default to '?'
            price = f"${crypto['quote']['USD']['price']:.2f}"
            market_cap = f"${crypto['quote']['USD']['market_cap']:.2f}"
            volume_24h = f"${crypto['quote']['USD']['volume_24h']:.2f}"
            print(f"{icon:<5} {name:<20} {symbol:<10} {price:<15} {market_cap:<20} {volume_24h:<20}")
    else:
        print("Error: 'data' key not found in the response")

# Main loop to refresh data every 30 seconds
def main():
    while True:
        data = get_crypto_data()
        if data:
            display_crypto_data(data)
        time.sleep(30)

if __name__ == "__main__":
    main()