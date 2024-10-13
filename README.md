# crpy
This Python script fetches and displays the latest cryptocurrency data from the CoinMarketCap API. It refreshes the data every 30 seconds and presents it in a clean, tabular format with icons for each currency.

# Features

- Fetches real-time cryptocurrency data from the CoinMarketCap API.
- Automatically refreshes data every 30 seconds.
- Displays data in a tabular format for easy reading.
- Includes icons for each cryptocurrency for visual identification.

# Installation

To install the necessary dependencies, ensure you have Python installed and run:

```sh
pip install -r requirements.txt
```

# Usage

To run the script, simply execute:

```sh
python crpy.py
```

This will start fetching and displaying the latest cryptocurrency data.

# Configuration

You need to configure the script with your CoinMarketCap API key. You can add the API key directly to the `.py` file.

## Adding API Key

To use the CoinMarketCap API, you will need an API key. You can obtain one by signing up on the CoinMarketCap website: [CoinMarketCap API](https://coinmarketcap.com/api/)

Open the `crpy.py` file and add your API key:

```python
# crpy.py
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'your_api_key_here',  # Your CoinMarketCap API key
}
```

Replace `'your_api_key_here'` with your actual API key.

# Contributing

If you would like to contribute to the project, please fork the repository and create a pull request. We welcome all contributions, including bug fixes, feature requests, and documentation improvements.
