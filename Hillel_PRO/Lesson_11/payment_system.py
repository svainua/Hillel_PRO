from abc import ABC, abstractmethod
from dataclasses import asdict

from api import PayPalAPI, StripeAPI
from models import Card, Product, User

STRIPE_ACCESS_TOKEN = "WEIFUHWEFUIHEWFIUWFEH"
PAYPAL_CREDENTIALS = {"username": "hillel", "password": "hillel123"}


def catch_errors(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            print(f"Error catched: {error}")

    return inner


class PaymentProvider(ABC):
    def __init__(self, user: User) -> None:
        self.user: User = user

    @abstractmethod
    def authorize(self, **kwagrs):
        pass

    @abstractmethod
    def checkout(self, product: Product):
        pass

    @abstractmethod
    def healthcheck(self) -> None:
        pass


class StripePaymentProvider(PaymentProvider):
    def authorize(self, **kwagrs):
        token = kwagrs.get("token", "")
        StripeAPI.authorize(
            token=token,
            user_email=self.user.email,
            card_number=self.user.card.number,
            expire_date=self.user.card.expire_date,
            cvv=self.user.card.cvv,
        )

    def checkout(self, product: Product):
        StripeAPI.checkout(user_email=self.user.email, price=product.price)

    def healthcheck(self):
        if StripeAPI.healthcheck() is False:
            raise Exception("Stripe is NOT AVAILABLE")


class PayPalPaymentProvider(PaymentProvider):

    def authorize(self, **kwagrs):
        username = kwagrs.get("username", "")
        password = kwagrs.get("password", "")
        PayPalAPI.authorize(
            username=username,
            password=password,
            email=self.user.email,
            card_data=asdict(self.user.card),
        )

    def checkout(self, product: Product):
        PayPalAPI.checkout(email=self.user.email, price=product.price)

    def healthcheck(self):
        if PayPalAPI.is_available() is False:
            raise Exception("Stripe is NOT AVAILABLE")


def provider_dispatcher(name: str, user: User) -> PaymentProvider:
    if name == "stripe":
        return StripePaymentProvider(user=user)  # noqa
    elif name == "paypal":
        return PayPalPaymentProvider(user=user)  # noqa
    else:
        raise Exception(f"Provider {name} is not supported")


def main():
    john = User(
        id_=1,
        email="John@mail.com",
        age=33,
        card=Card(number=1232343223455432, expire_date="12/26", cvv=234),
    )
    marry = User(
        id_=2,
        email="Marry@mail.com",
        age=20,
        card=Card(number=9876543987654398, expire_date="10/30", cvv=765),
    )

    samsung = Product(name="Samsung", price=1000)
    iphone = Product(name="iPhone", price=2000)

    stripe_credentials = {"token": STRIPE_ACCESS_TOKEN}

    payment_provider: PaymentProvider = provider_dispatcher(
        name="stripe", user=john
    )
    payment_provider.healthcheck()
    payment_provider.authorize(**stripe_credentials)
    payment_provider.checkout(product=samsung)

    payment_provider: PaymentProvider = provider_dispatcher(
        name="paypal", user=marry
    )
    payment_provider.healthcheck()
    payment_provider.authorize(**PAYPAL_CREDENTIALS)
    payment_provider.checkout(product=iphone)


if __name__ == "__main__":
    main()
