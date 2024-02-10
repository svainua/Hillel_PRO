currency_exchange: dict = {
    "USD": 0.87,
    "EUR": 0.94,
    "UAH": 0.023,
    "JPY": 0.0059,
    "CHF": 1,
}


class Price:
    def __init__(self, value: int, currency: str) -> None:
        self.value: int = value
        self.currency: str = currency

    def __str__(self):
        return f"{self.currency} {self.value}"

    def __add__(self, other) -> "Price":
        if self.currency == other.currency:
            return Price(self.value + other.value, self.currency)
        else:
            self.value = self.value * currency_exchange[self.currency]
            other.value = other.value * currency_exchange[other.currency]
            return Price(
                round(
                    (self.value + other.value)
                    / currency_exchange[self.currency],
                    2,
                ),
                self.currency,
            )

    def __sub__(self, other) -> "Price":
        if self.currency == other.currency:
            return Price(self.value - other.value, self.currency)
        else:
            self.value = self.value * currency_exchange[self.currency]
            other.value = other.value * currency_exchange[other.currency]
            return Price(
                round(
                    (self.value - other.value)
                    / currency_exchange[self.currency],
                    2,
                ),
                self.currency,
            )


value_1, currency_1 = input(
    "What's the price and the currency of the 1st product? [price currency]: "
).split(" ")
value_2, currency_2 = input(
    "What's the price and the currency of the 2nd product? [price currency]: "
).split(" ")

product_1: Price = Price(value=int(value_1), currency=currency_1)
product_2: Price = Price(value=int(value_2), currency=currency_2)

total: Price = product_1 + product_2

print(f"You should pay {total}")
