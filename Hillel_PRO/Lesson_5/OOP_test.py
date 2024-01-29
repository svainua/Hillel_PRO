class Item:
    pay_rate = 0.8  # The pay after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater or equal to zero!"
        assert (
            quantity >= 0
        ), f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        return self.price * self.pay_rate


item_1 = Item("Phone", 100, 1)
item_2 = Item("Laptop", 1000, 3)

# print(item_1.calculate_total_price())
# print(item_2.calculate_total_price())

# print(Item.__dict__) # All the attrributes for Class method
# print(item_1.__dict__) # All the attrributes for Class method

# print(item_1.apply_discount())

# item_2.pay_rate = 0.5
# print(item_2.apply_discount())

item_3 = Item("Cable", 10, 5)
item_4 = Item("Mouse", 50, 5)
item_5 = Item("Keyboard", 75, 5)

print(Item.all)

for instance in Item.all:
    print(instance.name)
