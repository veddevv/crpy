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
import curses

# Dictionary to map currency symbols to icons
currency_icons = {
    'BTC': '₿',
    'ETH': 'Ξ',
    'XRP': '✕',
    'LTC': 'Ł',
    'BCH': 'Ƀ',
    'XMR': 'ɱ',
    'DOGE': 'Ð',
    'SOL': '☀',
    'MATIC': '⬢',
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
def display_crypto_data(stdscr, data, previous_prices, update_interval):
    stdscr.clear()
    stdscr.addstr(0, 0, "Cryptocurrency Prices")
    stdscr.addstr(1, 0, f"Next update in: {update_interval} seconds")
    row = 3
    for currency in data:
        symbol = currency['symbol']
        price = currency['quote']['USD']['price']
        market_cap = currency['quote']['USD']['market_cap']
        volume_24h = currency['quote']['USD']['volume_24h']
        percent_change_24h = currency['quote']['USD']['percent_change_24h']
        icon = currency_icons.get(symbol, '')
        change = ''
        if symbol in previous_prices:
            if price > previous_prices[symbol]:
                change = '↑'
            elif price < previous_prices[symbol]:
                change = '↓'
        stdscr.addstr(row, 0, f"{icon} {symbol}: ${price:.2f} {change}")
        stdscr.addstr(row + 1, 0, f"    Market Cap: ${market_cap:.2f}")
        stdscr.addstr(row + 2, 0, f"    24h Volume: ${volume_24h:.2f}")
        stdscr.addstr(row + 3, 0, f"    24h Change: {percent_change_24h:.2f}%")
        previous_prices[symbol] = price
        row += 5
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    previous_prices = {}
    update_interval = 30
    while True:
        data = get_crypto_data()
        for i in range(update_interval, 0, -1):
            display_crypto_data(stdscr, data, previous_prices, i)
            time.sleep(1)

if __name__ == "__main__":
    curses.wrapper(main)
