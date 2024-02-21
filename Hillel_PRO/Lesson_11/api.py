import random
import uuid


class StripeAPI:
    authorization_state: dict[str, bool] = {}

    @staticmethod
    def healthcheck() -> bool:
        value = random.randint(1, 10)
        if value < 5:
            return True
        else:
            return False

    @classmethod
    def authorise(
        cls,
        token: str,
        user_email: str,
        card_number: int,
        expire_date: str,
        cvv: int,
    ) -> None:
        if token != "WEIFUHWEFUIHEWFIUWFEH":
            cls.authorization_state[user_email] = False
            raise Exception("Stripe authorisation error")
        else:
            cls.authorization_state[user_email] = True

    @classmethod
    def checkout(cls, user_email: str, price: int) -> str:
        if cls.authorization_state.get(user_email, False) is False:
            raise Exception("Stripe authorisation error")
        else:
            print(f"Checking out with Stripe for {price}$")
            payment_id = uuid.uuid4()
            return str(payment_id)


class PayPalAPI:
    authorization_state: dict[str, bool] = {}

    @staticmethod
    def is_available() -> bool:
        value = random.randint(1, 10)
        if value < 5:
            return True
        else:
            return False

    @classmethod
    def authorise(
        cls, username: str, email: str, password: str, card_data: dict
    ) -> None:
        if username == "hillel" and password == "hillel123":
            cls.authorization_state[email] = True
            return
        else:
            raise Exception("PayPal authorization error")

    @classmethod
    def checkout(cls, email: str, price: int) -> str:
        if cls.authorization_state.get(email, False) is False:
            raise Exception("PayPal authorisation error")
        else:
            print(f"Checking out with PayPal for {price}$")
            payment_id = uuid.uuid4()
            return str(payment_id)
