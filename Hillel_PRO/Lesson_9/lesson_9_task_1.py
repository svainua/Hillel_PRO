#   class Price:
#     def __init__(self, value: int, currency: str) -> None:
#       self.value: int = value
#       self.currency: str = currency


# Stripe
# 100 UAH -> CFH


currency_exchange: dict = {
    "USD": 0.87,
    "EUR": 0.94,
    "UAH": 0.023,
    "JPY": 0.0059,
    "CHF": 1,
}


class Price:
    def __init__(self, value: int, currency: str):
        self.value: int = value
        self.currency: str = currency

    def __str__(self):
        return f"{self.currency} {self.value}"

    def __add__(self, other) -> "Price":
        if self.currency == other.currency:
            return self.value + other.value
        else:
            self.value = self.value * currency_exchange[self.currency]
            other.value = other.value * currency_exchange[other.currency]
            return round(
                (self.value + other.value) / currency_exchange[self.currency],
                2,
            )

    def __sub__(self, other) -> "Price":
        if self.currency == other.currency:
            return self.value - other.value
        else:
            self.value = self.value * currency_exchange[self.currency]
            other.value = other.value * currency_exchange[other.currency]
            return round(
                (self.value - other.value) / currency_exchange[self.currency],
                2,
            )


class Product:
    def __init__(self, name: str, price: Price):
        self.name = name
        self.price = price


class PaymentProcessor:  # класс проводит оплату
    def checkout(self, product: Product, price: Price):  # сделать оплату
        pass


value_1, currency_1 = "500 UAH".split(" ")
value_2, currency_2 = "200 USD".split(" ")

product_1: Price = Price(value=int(value_1), currency=currency_1)
product_2: Price = Price(value=int(value_2), currency=currency_2)

total: Price = product_1 + product_2

print(total)
