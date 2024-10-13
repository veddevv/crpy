"""
Author: Matheo Alexander
Date: 13.10.2024
Description: This script fetches and displays the latest cryptocurrency data from the CoinMarketCap API.
             It refreshes the data every 30 seconds and displays it in a clean, tabular format with icons for each currency.
                You need to sign up for a free CoinMarketCap API key to use this script.
usage: python crpy.py
"""

import requests
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
    'XMR': 'ɱ',
    'DOGE': 'Ð',
    'DOT': '●',
    'UNI': '🦄',
    'LINK': '🔗',
    'SOL': '☀',
    'AVAX': '❄',
    'MATIC': '⬢',
    'ATOM': '⚛',
    'VET': 'V',
    'FIL': '⛓',
    'ICP': '🌀',
    'AAVE': '👻',
    'ALGO': '⎇',
    'XTZ': 'ꜩ',
    'THETA': 'Θ',
    'FTM': '👻',
    'HBAR': 'ℏ',
    'NEO': '◎',
    'KSM': '🪶',
    'EGLD': '🛡',
    'CAKE': '🍰',
    'SHIB': '🐕',
    'SUSHI': '🍣',
    'MANA': '🗺',
    'AXS': '🪓',
    'ENJ': '🎮',
    'CHZ': '🌶',
    'ZIL': '⚡',
    'GRT': '🧠',
    '1INCH': '📏',
    'BAT': '🦇',
    'REN': '🌀',
    'YFI': '🌾',
    'LUNA': '🌕',
    'FTT': '🦈',
    'CEL': '🔥',
    'RSR': '💱',
    'COMP': '🏦',
    'KNC': '🗡',
}

# Function to get cryptocurrency data from CoinMarketCap API
def get_crypto_data():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'your_api_key_here',
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['data']

# Function to display cryptocurrency data
def display_crypto_data(data, previous_prices):
    os.system('cls' if os.name == 'nt' else 'clear')
    for currency in data:
        symbol = currency['symbol']
        price = currency['quote']['USD']['price']
        icon = currency_icons.get(symbol, '')
        change = ''
        if symbol in previous_prices:
            if price > previous_prices[symbol]:
                change = '↑'
            elif price < previous_prices[symbol]:
                change = '↓'
        print(f"{icon} {symbol}: ${price:.2f} {change}")
        previous_prices[symbol] = price

def main():
    previous_prices = {}
    while True:
        data = get_crypto_data()
        display_crypto_data(data, previous_prices)
        time.sleep(30)

if __name__ == "__main__":
    main()
