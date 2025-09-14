import requests

response = requests.get("https://open.er-api.com/v6/latest/USD")

# Get the latest conversion rate from USD to PHP
data = response.json()
usd_to_php_rate = data['rates']['PHP']
print(usd_to_php_rate)
