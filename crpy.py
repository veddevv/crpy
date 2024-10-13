"""
Author: Matheo Alexander
Date: 13.10.2024
Description: This script fetches and displays the latest cryptocurrency data from the CoinMarketCap API.
             It refreshes the data every 30 seconds and displays it in a clean, tabular format with icons for each currency.
                You need to sign up for a free CoinMarketCap API key to use this script.
usage: python crpy.py
"""

import requests
import matplotlib.pyplot as plt
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
            print(f"{crypto['cmc_rank']:<5} {crypto['name']:<20} {crypto['symbol']:<10} {crypto['quote']['USD']['price']:<15.2f} {crypto['quote']['USD']['market_cap']:<20.2f} {crypto['quote']['USD']['volume_24h']:<20.2f}")

# Function to update the chart
def update_chart(prices, names):
    plt.clf()
    plt.bar(names, prices)
    plt.xlabel('Cryptocurrency')
    plt.ylabel('Price (USD)')
    plt.title('Cryptocurrency Prices')
    plt.pause(0.1)

# Main function to periodically update data and chart
def main():
    plt.ion()
    while True:
        data = get_crypto_data()
        if data:
            display_crypto_data(data)
            prices = [crypto['quote']['USD']['price'] for crypto in data['data']]
            names = [crypto['name'] for crypto in data['data']]
            update_chart(prices, names)
        time.sleep(10)

if __name__ == "__main__":
    main()
