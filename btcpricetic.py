import requests
bitcoin_api_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

def get_latest_bitcoin_price():
    response = requests.get(bitcoin_api_url)
    response_json  = response.json()
    return float(response_json['bitcoin']['usd'])



















