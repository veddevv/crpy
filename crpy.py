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
from rich.console import Console
from rich.table import Table
from rich.live import Live

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

# Function to create a table with cryptocurrency data
def create_table(data, previous_prices):
    table = Table(title="Cryptocurrency Prices")
    table.add_column("Icon", justify="center")
    table.add_column("Symbol", justify="center")
    table.add_column("Price (USD)", justify="right")
    table.add_column("Market Cap (USD)", justify="right")
    table.add_column("24h Volume (USD)", justify="right")
    table.add_column("24h Change (%)", justify="right")
    table.add_column("Change", justify="center")

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
        table.add_row(
            icon,
            symbol,
            f"${price:.2f}",
            f"${market_cap:.2f}",
            f"${volume_24h:.2f}",
            f"{percent_change_24h:.2f}%",
            change
        )
        previous_prices[symbol] = price

    return table

def main():
    console = Console()
    previous_prices = {}
    update_interval = 30

    with Live(console=console, refresh_per_second=1) as live:
        while True:
            data = get_crypto_data()
            for i in range(update_interval, 0, -1):
                table = create_table(data, previous_prices)
                live.update(table)
                time.sleep(1)

if __name__ == "__main__":
    main()
