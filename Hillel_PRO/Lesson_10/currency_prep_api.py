import datetime
import json
from dataclasses import dataclass

import requests

MIDDLE_CURRENCY = "CHF"
ALPHA_VANTAGE_API_KEY = "H7CYK4OLE6Z4MEN0"

fulldate = datetime.datetime.now()
timestamp: str = fulldate.strftime("%d/%m/%Y at %H:%M:%S")

results = {"results": []}


@dataclass
class Price:
    value: float
    currency: str

    def __add__(self, other: "Price") -> "Price":
        if self.currency == other.currency:
            return Price(
                value=(self.value + other.value), currency=self.currency
            )

        left_in_middle: float = convert(
            value=self.value,
            currency_from=self.currency,
            currency_to=MIDDLE_CURRENCY,
        )

        right_in_middle: float = convert(
            value=other.value,
            currency_from=other.currency,
            currency_to=MIDDLE_CURRENCY,
        )

        total_in_middle: float = left_in_middle + right_in_middle
        total_in_left_currency: float = convert(
            value=total_in_middle,
            currency_from=MIDDLE_CURRENCY,
            currency_to=self.currency,
        )

        return Price(value=total_in_left_currency, currency=self.currency)


def track_result(currency_from: str, currency_to: str, rate: float, date: str):
    content: dict = {
        "currency_from": currency_from,
        "currency_to": currency_to,
        "rate": rate,
        "timestamp": date,
    }
    results["results"].append(content)


def convert(value: float, currency_from: str, currency_to: str) -> float:
    URL = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={currency_from}&to_currency={currency_to}&apikey={ALPHA_VANTAGE_API_KEY}"  # noqa
    response: requests.Response = requests.get(URL)
    result: dict = response.json()
    coefficient: float = float(
        result["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    )
    track_result(
        currency_from=currency_from,
        currency_to=currency_to,
        rate=coefficient,
        date=timestamp,
    )
    return round(value * coefficient, 2)


flight = Price(value=200, currency="USD")
hotel = Price(value=1000, currency="UAH")

total: Price = flight + hotel
print(total)

with open("logs.json", mode="a") as file:
    json.dump(results, file, indent=4)
