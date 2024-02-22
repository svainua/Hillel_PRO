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


@catch_errors
def checkout(user: User, product: Product, payment_provider: str):
    if payment_provider == "stripe":
        StripeAPI.authorize(
            user_email=user.email,
            token=STRIPE_ACCESS_TOKEN,
            card_number=user.card.number,
            expire_date=user.card.expire_date,
            cvv=user.card.cvv,
        )

        StripeAPI.checkout(user_email=user.email, price=product.price)

    elif payment_provider == "paypal":
        PayPalAPI.authorize(
            username=PAYPAL_CREDENTIALS["username"],
            password=PAYPAL_CREDENTIALS["password"],
            email=user.email,
            card_data=asdict(user.card),
        )

        PayPalAPI.checkout(email=user.email, price=product.price)


def startup_check(payment_provider: str):
    if payment_provider == "stripe":
        available: bool = StripeAPI.healthcheck()
    elif payment_provider == "paypal":
        available: bool = PayPalAPI.is_available()

    if available is False:
        print(f"Payment provider {payment_provider} is NOT AVAILABLE")
    else:
        print(f"Payment provider {payment_provider} is AVAILABLE")


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

    startup_check(payment_provider="paypal")
    startup_check(payment_provider="stripe")

    checkout(user=john, product=samsung, payment_provider="stripe")
    checkout(user=marry, product=iphone, payment_provider="paypal")


if __name__ == "__main__":
    main()
