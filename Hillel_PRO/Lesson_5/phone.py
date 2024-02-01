from item import Item


class Phone(Item):
    def __init__(
        self,
        name: str,
        price: float,
        quantity: int = 0,
        broken_phones: int = 0,
    ):
        # Call for super function to have access to all attributes / methods
        super().__init__(name, price, quantity)
        # Run validations to the received arguments
        assert (
            broken_phones >= 0
        ), f"Broken phone {price} is not greater or equal to zero!"

        # Assign to self object
        self.broken_phones = broken_phones


# phone_1 = Phone("jvcPhone10",500,5,1)

# print(Item.all)
# print(Phone.all)
