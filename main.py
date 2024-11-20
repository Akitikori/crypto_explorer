import requests

crypto_name = input("What cryptocurrency are you interested in? ").strip().lower()
currency = "usd"

url = f"http://api.coingecko.com/api/v3/simple/price?ids={crypto_name}&vs_currencies={currency}"

response = requests.get(url)

if response.status_code == 200:
    price = response.json()
    if crypto_name in price:
        print(f"The current price of {crypto_name.capitalize()} in {currency.upper()} is {price[crypto_name][currency]}")
    else:
        print(f"Cryptocurrency {crypto_name} was not found. Please check the name and try again")
else:
    print(f"Failed to fetch repositories. Status code: {response.status_code}")

