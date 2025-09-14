import requests

response = requests.get("https://open.er-api.com/v6/latest/USD")

# Get the latest conversion rate from USD to PHP
print(response.json())
conversion_rate = response.json()['rates']['PHP']
