from dataclasses import dataclass

EXCHANGE_RATE = {
    "usd": {"chf": 1.3, "uah": 0.3},
    "uah": {"usd": 38, "chf": 40},
    "chf": {"chf": 1, "usd": 0.3, "auh": 0.023},
}

MIDDLE_CURRENCY = "chf"


def convert(value: float, currency_from: str, currency_to: str) -> float:
    coefficient: float = EXCHANGE_RATE[currency_from][currency_to]
    return value * coefficient


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


flight = Price(value=200, currency="usd")
hotel = Price(value=1000, currency="uah")

total: Price = flight + hotel
print(total)
