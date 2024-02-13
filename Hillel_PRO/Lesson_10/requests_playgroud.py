import requests

# url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=XSN17SDSA5RAM5W2"
# response = requests.get(url).json()

# print(response)
currency_from = "USD"
currency_to = "UAH"

API_KEY = "XSN17SDSA5RAM5W2"
response: requests.Response = requests.get(
    f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={currency_from}&to_currency={currency_to}&apikey={API_KEY}"
).json()
coefficient = response["Realtime Currency Exchange Rate"]["5. Exchange Rate"]

print(response)
# print(coefficient)
