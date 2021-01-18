import requests
import time
from datetime import datetime






bitcoin_api_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/{}/with/key/glYhDZin0pvxxGJNr7GwSarDPpATCaOa7eTYJAQkR97'

def get_latest_bitcoin_price():
    response = requests.get(bitcoin_api_url)
    response_json  = response.json()
    return float(response_json['bitcoin']['usd'])

# BITCOIN_PRICE_THRESHOLD = get_latest_bitcoin_price()
BITCOIN_PRICE_THRESHOLD = 40000


percentage_change = float(input('what percentage change do you want an alert'
                                '?'))

percentage_value =( BITCOIN_PRICE_THRESHOLD / 100 ) * percentage_change

print (str('BTC price at time of setting up alert ') + (str(BITCOIN_PRICE_THRESHOLD)))
print(str('when the price drops by ') + str(percentage_value) + str(' to a value of ') + str(BITCOIN_PRICE_THRESHOLD - percentage_value) + str(' you will get an alert'))


def post_ifttt_webhook(event, value):
    # The payload that will be sent to IFTTT service
    data = {'value1': value}
    # inserts our desired event
    ifttt_event_url = IFTTT_WEBHOOKS_URL.format(event)
    # Sends a HTTP POST request to the webhook URL
    requests.post(ifttt_event_url, json=data)


    # Sends a HTTP POST request to the webhook URL
    requests.post(ifttt_event_url, json=data)


def format_bitcoin_history(bitcoin_history):
    rows = []
    for bitcoin_price in bitcoin_history:
        # Formats the date into a string: '24.02.2018 15:09'
        date = bitcoin_price['date'].strftime('%d.%m.%Y %H:%M')
        price = bitcoin_price['price']
        # <b> (bold) tag creates bolded text
        # 24.02.2018 15:09: $<b>10123.4</b>
        row = '{}: $<b>{}</b>'.format(date, price)
        rows.append(row)

    # Use a <br> (break) tag to create a new line
    # Join the rows delimited by <br> tag: row1<br>row2<br>row3
    return '<br>'.join(rows)



def main():
    bitcoin_history = []
    while True:
        price = get_latest_bitcoin_price()
        date = datetime.now()
        bitcoin_history.append({'date': date, 'price': price})

        # Send an emergency notification
        if price <=  BITCOIN_PRICE_THRESHOLD - percentage_value:

            post_ifttt_webhook('bitcoin_price_emergency', price)

        # Send a Telegram notification
        # Once we have 5 items in our bitcoin_history send an update
        if len(bitcoin_history) == 5:
            post_ifttt_webhook('bitcoin_price_update',
                               format_bitcoin_history(bitcoin_history))
            # Reset the history
            bitcoin_history = []

        # Sleep for 5 minutes
        # (For testing purposes you can set it to a lower number)
        time.sleep(5 * 60)
    pass

if __name__ == '__main__':
    main()














