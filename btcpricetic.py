

import requests
userinput = input('please type your cryto');
usercurrency = input('please type your currency');


# bitcoin_api_url = "https://api.coingecko.com/api/v3/simple/price?ids="+ str(userinput) + "&vs_currencies=usd"
bitcoin_api_url = "https://api.coingecko.com/api/v3/simple/price?ids="+str(userinput)+ "&vs_currencies="+str(usercurrency)+""
response = requests.get(bitcoin_api_url)
bitcoinprice = response.json()

bitcoinvalue = bitcoinprice[str(userinput)][str(usercurrency)]

print(bitcoinvalue)

# print (bitcoinprice)










